# encoding: utf-8

import sys
from struct import pack, unpack
from array import array

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
    data_out = array('c')
    tmp = ''
    for elem in input_array:
        tmp += code(elem)

    return data_out.fromstring(tmp)

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

    

#a = [1, 130, 332, 412345, 234, 2345, 123]
#print len(code_list(a))
#print uncode_buffer(code_list(a))
