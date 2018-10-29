import re
import sys
import md5
from tree_class import *
sys.path.insert(0, '../archive')
# TODO load dic from file
# from archive import dic
import simple9
import varbyte 

# TEST
from test_data import *

def tokenize(query):
    tmp_list = re.findall(r'\w+|[\(\)\|&!]', query)
    token_list = []
    priority = 0
    for raw_token in tmp_list:
        if re.match('\w+', raw_token):
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


def get_stream(word):
    # TODO load dic from file,
    # dic = read_dict('filepath')
    #global dic

    # TODO give choise of compress algorythm, change hash algo
    #compressed = md5.new(word).digest()
    #return varbyte.decode_array(dic.get(compressed))
    return dic.get(word)

def activate_node(node, betta):
    if node is not None:
        if isinstance(node, word_node):
            node.stream = get_stream(node.value)
            # print node.stream
        if isinstance(node, not_node):
            node.max_pos = betta
        activate_node(node.left, betta)
        activate_node(node.right, betta)

def execute(root):
    # change to load from file
    # global doc_id

    out_data = []
    value = 1
    valid = True
    new_value = 0
    prev = 0

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
   
    # return [doc_id[idx - 1] for idx in id_set]
    return out_data 

def parse(query):
    query = query.replace(' ', '')
    token_list = tokenize(query)
    root = parse_list(token_list)
    return root
