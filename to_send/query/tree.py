#!usr/bin/python2
# vim : set fileencoding=utf-8 :
# coding : utf-8
# Kononov Sergey BD-21

import re
import sys
import md5
from tree_class import *
sys.path.insert(0, 'archive')
import simple9
import varbyte 

# TEST MODE
# from test_data import *
rus = r'[абвгдеёжзийклмнопрстуфхцчшщъчьыэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЧЬЫЭЮЯ\w]+'

def tokenize(query):
    tmp_list = re.findall(rus + '|[\(\)\|&!]', query)
    token_list = []
    priority = 0
    for raw_token in tmp_list:
        if re.match(rus, raw_token):
            token_list.append(word_node(raw_token, priority))
        elif raw_token == '(':
            priority += 5
        elif raw_token == ')':
            priority -= 5
        elif raw_token == '|':
            token_list.append(or_node(priority))
        elif raw_token == '&':
            token_list.append(and_node(priority))
        elif raw_token == '!':
            token_list.append(not_node(priority))
   
    return  token_list

def parse_list(token_list):
    if len(token_list) == 1:
        return token_list[0]
    
    pos = 0
    min_priority = token_list[0].priority
    for i, token in enumerate(token_list[1:]):
        if token.priority <= min_priority:
            min_priority = token.priority
            pos = i + 1

    if isinstance(token_list[pos], not_node):
        left = None
    else:
        left = parse_list(token_list[:pos])
    right = parse_list(token_list[pos + 1:])

    token_list[pos].left = left
    token_list[pos].right = right

    return token_list[pos]

class Decoder(object):
    def __init__(self, archive_type):
        if archive_type == 'varbyte':
            self.decode = varbyte.decode_array
        else:
            self.decode = varbyte.decode_array
            # self.decode = simple9.decode

def get_stream(word, dic, decode):
    compressed = md5.new(word).digest()
    code_list = dic.get(compressed)
    if code_list:
        return decode.decode(code_list)
    else:
        return []

def activate_node(node, betta, dic, decode):
    if node is not None:
        if isinstance(node, word_node):
            node.stream = get_stream(node.value, dic, decode)
        if isinstance(node, not_node):
            node.max_pos = betta
        activate_node(node.left, betta, dic, decode)
        activate_node(node.right, betta, dic, decode)

def execute(root):
    out_data = []
    value, new_value, prev = 1, 0, 0
    valid = True

    while prev != value:
        root.go_to(value)
        new_value, valid = root.evaluate()
        if valid:
            out_data.append(new_value)
        
        prev = value
        if new_value != value:
            value = new_value
        if valid:
            value += 1
   
    return out_data 

def parse(query):
    query = query.replace(' ', '').decode('utf-8').lower().encode('utf-8')
    token_list = tokenize(query)
    root = parse_list(token_list)
    return root
