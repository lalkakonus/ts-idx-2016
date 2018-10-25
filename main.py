# encoding: utf-8

from docreader import *
from parser import *
from archive import index_data


if __name__ == '__main__':
    reader = DocumentStreamReader(parse_command_line().files)
    
    index_data(reader)

    # N = 2000
    # LENGTH = 200
    # loop = iter(reader)
    # for i in range(N):
    #     doc = next(loop)
    #     print 'Doc # ', i,': ', doc.text[:LENGTH]
    #     text  = extract_words(doc.text[:LENGTH])
    #     index_doc(doc.url, text)

    print parse_query('в')
