# encoding: utf-8
# Kononov Sergey BD-21

import sys
from struct import pack, unpack
from array import array

# TEST MODE
# import time
# import random

def code(data_in):
    mask = int(b'01111111', 2)
    data_out = 0
    byte_cnt = 0
    
    while data_in > 0:
        addition = (data_in & mask)
        addition = addition << (byte_cnt * 8)
        data_out |= addition
        
        if data_in > 128:
            flag = 1 << (7 + 8 * byte_cnt)
        else:
            flag = 0

        data_out |= flag
        data_in = data_in >> 7
        byte_cnt += 1

    return pack('q', data_out)[:byte_cnt] # pack to long long

def code_array(input_array):
    tmp = ''
    for elem in input_array:
        tmp += code(elem)

    return array('c', tmp)

def decode(code):
    data_out = 0
    mask = int(b'01111111', 2)

    for pos, byte in enumerate(code):
        addition = bytearray(byte)[0]  & mask
        addition = addition << (7 * pos)
        data_out |= addition
    
    return int(data_out)


def decode_array(binary_data):
    mask = int(b'10000000', 2)

    array_length = len(binary_data)
    fmt = str(array_length) + 'c'
    char_data = unpack(fmt, binary_data)
    
    compressed = []
    compressed.append('')
    for char in char_data:
        compressed[-1] += char
        if (bytearray(char)[0] & mask) == 0:
            compressed.append('')

    compressed.remove('')
    
    out_data = []
    for elem in compressed:
        out_data.append(decode(elem))

    return out_data

    
# TEST
#
# test = range(1, 10000)
# random.shuffle(test)
# 
# t1 = time.time()
# test_sum = bool(test == decode_array(code_array(test)))
# t2 = time.time()
# 
# t3 = time.time()
# for i in range(1, 10000):
#     test_sum |= i == decode(code(i))
# t4 = time.time()
# 
# print 'varbyte tests :', test_sum * 'OK' + ~test_sum * 'ERROR'
# print '[1, 10000] array compressed and decmpressed in', t2 - t1
# print '[1, 10000] ints compressed and decmpressed in', t4 - t3
