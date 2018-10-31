#!/usr/bin/env python
# Kononov Sergey BD-21

import sys, md5, varbyte, simple9
from doc2words import extract_words
from pickle_obj import save_obj

# ordered URLs
doc_id = []

# dict of hash(word) : varbyte_archive(array of doc_id)
dic = {}

def index_doc(url, text):
    global doc_id, dic

    doc_id.append(url)
    addition = len(doc_id)

    for word in text:
        key = md5.new(word.encode('utf-8')).digest()
        value = dic.get(key)
        if value is not None: 
            if value[-1] != addition:
                value.append(addition)
        else:
            value = [addition]
        dic.update({key: value})

def code_data(dic, archive_type):
    if archive_type == 'varbyte':
        code = varbyte.code_array
    else:
        code = varbyte.code_array
        # code = simple9.code
    for key in dic.keys():
        dic.update({key: code(dic.get(key))})

#def save_data(num):
#    code_data(dic, archive_type) 
#    save_obj([archive_type, dic], 'Data/compressed_dict_' + str(num) + '.pckl')

def index_data(reader, archive_type):
    global doc_id, dic
    num = 0

    for doc in reader:
        text  = extract_words(doc.text)
        index_doc(doc.url, text)

        num += 1
        #if not (num % 10000):
        #    print sys.getsizeof(dic) / (1024 * 1024)
#       if sys.getsizeof(dic) > 5e2:
#           save_data(num)
#           dic.clear()
#           num += 1

#    if len(dic):
    code_data(dic, archive_type) 
    save_obj([archive_type, dic], 'Data/compressed_dict.pckl')
#        save_data(num)
    save_obj([archive_type, doc_id], 'Data/compressed_id.pckl')

    # print '# Data sucsessefully copressed with', archive_type, 'and saved to:'
    # print '  * Data/compressed_dict.pckl'
    # print '  * Data/compressed_id.pckl'
    # print '# Total word amount :', len(dic)
    # print '# URLs processed :', len(doc_id)
