import re
import sys
import md5
from tree_class import *
import node_functions# import *
sys.path.insert(0, '../archive')
# TODO load dic from file
# from archive import dic
import simple9
import varbyte 

dic = {'a':[1,2,3,4,5],
       'b':[1,2,3,4],
       'c':[4,5,6,7]}


def tokenize(query):
    tmp_list = re.findall(r'\w+|[\(\)\|&!]', query)
    token_list = []
    priority = 0
    for raw_token in tmp_list:
        if re.match('\w+', raw_token):
            token_list.append(node('w', raw_token, priority + 4))
        elif raw_token == '(':
            priority += 5
        elif raw_token == ')':
            priority -= 5
        elif raw_token == '|':
            token_list.append(node('|', raw_token, priority + 1))
        elif raw_token == '&':
            token_list.append(node('&', raw_token, priority + 2))
        elif raw_token == '!':
            token_list.append(node('!', raw_token, priority + 3))
   
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

    if token_list[pos].class_type == '!':
        left = None
    else:
        left = parse_list(token_list[:pos])
    right = parse_list(token_list[pos + 1:])

    node = token_list[pos]
    node.add_left(left)
    node.add_right(right)

    return node

def parse(query):
    query = query.replace(' ', '')
    token_list = tokenize(query)
    root = parse_list(token_list)
    # root.print_tree()
    return root

def get_stream(word):
    # TODO load dic from file,
    # dic = read_dict('filepath')
    global dic

    # TODO give choise of compress algorythm, change hash algo
    #compressed = md5.new(word).digest()
    #return varbyte.decode_array(dic.get(compressed))
    return dic.get(word)

def activate_node(node):
    global node_functions

    if node is not None:
        node.evaluate = node_functions.functions.get(node.class_type)[0]
        node.go_to = node_functions.functions.get(node.class_type)[1]
        if node.class_type == 'w':
            node.stream = get_stream(node.value)
        activate_node(node.left)
        activate_node(node.right)

def execute(root):
    # change to load from file
    # global doc_id

    out_data = []
    value = 1
    prev_valid = True
    valid = True
    new_value = 0

    while new_value != value:
        root.go_to(value)
        new_value, valid = root.evaluate()
        if valid:
            res.append(new_value)
        if new_value == value:
            value += 1
        else:
            value = new_value
    
    # return [doc_id[idx - 1] for idx in id_set]
    return out_data 


a = 'a'
root = parse(a)
#root.print_node()
activate_node(root)
execute(root)
