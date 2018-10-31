#!usr/bin/env python
# Kononov Sergey BD-21

from docreader import *
sys.path.insert(0, 'archive')
from archive import index_data
import os, re, shutil

# Create Data directory
if not os.access('Data', os.F_OK):
    os.mkdir('Data')

# Clear existance data
file_list = filter(lambda filename: re.match(r'.*\.pckl', filename),
                   os.listdir('Data'))
map(lambda filename: os.remove('Data/' + filename), file_list)

# Parse command line arguments and index data
if __name__ == '__main__':
    archivation_type = parse_command_line().archivation
    reader = DocumentStreamReader(parse_command_line().files)
    index_data(reader, archivation_type)
