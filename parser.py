# encoding: utf-8

from varbyte_code import *
import md5
from archive import dic, doc_id

def retrive_assosiated(word):
    global dic

    idxs = dic.get(md5.new(word).digest())
    
    if idxs is not None:
        return uncode_buffer(idxs)
    else:
        return None

def parse_query(query):
    global dic, doc_id

    query = query.replace(' ', '').split('&')

    compressed = md5.new(query[0]).digest()
    id_list = decode_array(dic.get(compressed))
    id_set = set(id_list)

    for word in query[1:]:
        compressed = md5.new(word).digest()
        id_list = decode_array(dic.get(compressed))
        id_list = id_set & set(id_list)
        id_set = set(id_list)

    # return '\n'.join([doc_id[idx - 1] for idx in id_set])
    # return [doc_id[idx - 1] for idx in id_set]
    return id_set
