from docreader import *

if __name__ == '__main__':
    reader = DocumentStreamReader(parse_command_line().files)
    # for doc in reader:
    doc = next(reader.__iter__())
    print doc.url
    print doc.text[:100]
    # print "%s\t%d bytes" % (doc.url, len(doc.text))
