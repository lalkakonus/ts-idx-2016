#!usr/bin/python2
# vim : set fileencoding=utf-8 :
# encoding : utf-8
# Kononov Sergey BD-21

import sys
sys.path.insert(0, 'archive')
sys.path.insert(0, 'query')
from tree import *
from pickle_obj import load_obj
import os

def load_data():
    # Check Data directory
    if not os.access('Data', os.F_OK):
        print 'Error, data not exist'
        return

    # Check existance data
    if not (os.access('Data/compressed_id.pckl', os.F_OK) and 
            os.access('Data/compressed_dict.pckl', os.F_OK)):
        print 'Error, data not exist'
        return

    dic = load_obj('Data/compressed_dict.pckl')
    doc_id = load_obj('Data/compressed_id.pckl')
    
    print '# Data sucsessefully load from Data directory'
    print '# Total word amount :', len(dic)
    print '# URLs count :', len(doc_id)
    
    return dic, doc_id, len(dic)

def execute_list(query_list, dic, doc_id, N):
    result_list = []
    for query in query_list:

        # query = 'в & !к'
        q_tree = parse(query)
        activate_node(q_tree, N, dic)
        id_set = execute(q_tree)
        #print id_set
        result = [doc_id[idx - 1] for idx in id_set]
        addition = [query, str(len(id_set)), '\n'.join(result)]
        result_list.append(addition)
    return result_list

def get_query_list():
    query_list = []

    line = raw_input('->')
    query_list.append(line)
    while line:
        line = raw_input('->')
        query_list.append(line)
    return filter(lambda x: x != '', query_list)

def print_result(result):
    for one in result:
        print one[0], '\n', one[1], '\n', one[2]

dic, doc_id, N = load_data()
query_list = get_query_list()
result = execute_list(query_list, dic, doc_id, N)
print_result(result)
