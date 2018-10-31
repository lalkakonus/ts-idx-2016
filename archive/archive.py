# Kononov Sergey BD-21

import md5
import varbyte
import simple9
from doc2words import extract_words
from pickle_obj import save_obj

# ordered URLs
doc_id = []

# dict of hash(word) : varbyte_archive(array of doc_id)
dic = {}

def index_doc(url, text):
    global doc_id, dic

    doc_id.append(url)
    addition = varbyte.code(len(doc_id))
    
    for word in text:
        key = md5.new(word.encode('utf-8')).digest()
        value = dic.get(key)
        if value is not None: 
            if value[-len(addition):] != addition:
                value += addition
        else:
            value = addition 
        dic.update({key: value})
    
def index_data(reader):
    global doc_id, dic

    for doc in reader:
      text  = extract_words(doc.text)
      index_doc(doc.url, text)
   
    # TEST MODE
    # N = 20
    # LENGTH = 200
    # loop = iter(reader)
    # for i in range(N):
    #     doc = next(loop)
    #     print 'Doc # ', i + 1,': ', doc.text[:LENGTH]
    #     text  = extract_words(doc.text[:LENGTH])
    #     index_doc(doc.url, text)
    
    save_obj(dic, 'Data/compressed_dict.pckl')
    save_obj(doc_id, 'Data/compressed_id.pckl')

    print '# Data sucsessefully copressed and saved to:'
    print '  * Data/compressed_dict.pckl'
    print '  * Data/compressed_id.pckl'
    print '# Total word amount :', len(dic)
    print '# URLs processed :', len(doc_id)
