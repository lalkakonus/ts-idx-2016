#!usr/bin/env python
# Kononov Sergey BD-21

from docreader import *
sys.path.insert(0, 'archive')
from archive import index_data
import os

# Create Data directory
if not os.access('Data', os.F_OK):
    os.mkdir('Data')

# Delete existance data
if os.access('Data/compressed_id.pckl', os.F_OK):
    os.remove('Data/compressed_id.pckl')

if os.access('Data/compressed_dic.pckl', os.F_OK):
    os.remove('Data/compressed_dic.pckl')

if __name__ == '__main__':
    archivation_type = parse_command_line().archivation
    reader = DocumentStreamReader(parse_command_line().files)
    index_data(reader, archivation_type)
