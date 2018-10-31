#!usr/bin/python2
# vim : set fileencoding=utf-8 :
# Kononov Sergey BD-21

from docreader import *
sys.path.insert(0, 'archive')
from archive import index_data
import os

# Create Data directory
if not os.access('Data', os.F_OK):
    os.mkdir('Data')

# Delete existance data
if os.access('Data/compressd_id.pckl', os.F_OK):
    os.remove('Data/compressd_id.pckl')
    os.remove('Data/compressd_dic.pckl')

if __name__ == '__main__':
    reader = DocumentStreamReader(parse_command_line().files)
    index_data(reader)
