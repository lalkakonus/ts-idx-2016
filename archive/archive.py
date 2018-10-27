# encoding: utf-8

import md5
from varbyte import *
from doc2words import extract_words

# ordered URLs
doc_id = []

# dict of hash(word) : varbyte_archive(array of doc_id)
dic = {}

def index_doc(url, text):
    global doc_id, dic

    doc_id.append(url)
    addition = code(len(doc_id))
    
    for word in text:
        key = md5.new(word.encode('utf-8')).digest()
        value = dic.get(key)
        if value is not None: 
            value += addition
        else:
            value = addition 
        # print 'Add [', word, '] :', value, ';'
        dic.update({key: value})
    
def index_data(reader):
    for doc in reader:
      text  = extract_words(doc.text)
      index_doc(doc.url, text)
    
    print '# Data sucsessefully copressed.'
    print '# Total word amount :', len(dic)
    print '# URLs processed :', len(doc_id)
