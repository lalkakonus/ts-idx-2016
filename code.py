import sys
from struct import pack, unpack
from array import array

def code_int(input_int):
    tmp = input_int
    mask = int(b'01111111', 2)
    result = 0
    byte_cnt = 0
    while tmp > 0:
        addition = (tmp & mask)
        addition = addition << (byte_cnt * 8)
        result = result | addition
        
        if tmp > 128:
            flag = 1 << (7 + 8 * byte_cnt)
        else:
            flag = 0

        result = result | flag
        tmp = tmp >> 7
        byte_cnt += 1

    return pack('q', result)[:byte_cnt] # pack to long long

def code_list(lst):
    result = array('c')
    tmp = ''
    for elem in lst:
        tmp += code_int(elem)

    result.fromstring(tmp)
    return result


def uncode_int(code):
    result = 0
    mask = int(b'01111111', 2)
    for i, byte in enumerate(code):
        addition = bytearray(byte)[0]  & mask
        addition = addition << (7 * i)
        result = result | addition
    return int(result)


def uncode_buffer(binary_data):
    
    buff_length = len(binary_data)
    fmt = str(buff_length) + 'c'
    char_data = unpack(fmt, binary_data)
    
    elements = []
    elements.append('')
    for char in cahr_data:
        elements[-1] += char
        if bytearray(char)[0] >> 7 == 0:
            elements.append('')

    elements.remove('')
    
    result = []
    for element in elements:
        result.append(uncode_int(element))

    return result

    

#a = [1, 130, 332, 412345, 234, 2345, 123]
#print len(code_list(a))
#print uncode_buffer(code_list(a))
