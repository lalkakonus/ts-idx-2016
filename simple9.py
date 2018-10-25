from struct import *

EXP = [1, 2, 3, 4, 5, 7, 9, 14, 28]
EXP_LEN = len(EXP)
BORDER = [2 ** x for x in EXP]
PAYLOAD_SIZE = 28

def define_size(value):
    global EXP, EXP_LEN, BORDER

    for idx in range(EXP_LEN):
        if value < BORDER[idx]:
            return EXP[idx]
    return None

def define_count(sequence):
    cnt = 0
    maximum = 0
    global PAYLOAD_SIZE
    
    for elem in sequence:
        cnt += 1
        maximum = max(maximum, define_size(elem))
        if maximum * cnt > PAYLOAD_SIZE:
            return cnt - 1
    
    # list is finish 
    return cnt

def code_word(sequence):
    cnt = define_count(sequence)
    round_cnt = 28
    pos = 0

    for i, x in enumerate(EXP): 
        if x > cnt:
            round_cnt = EXP[i - 1]
            break

    size = PAYLOAD_SIZE / round_cnt #EXP[pos]

    compressed = 0
    compressed |= round_cnt << PAYLOAD_SIZE
    for i in range(cnt):
        compressed |= sequence[i] << size * i

    return pack('i', compressed), cnt

def code(sequence):
    data_out = ''

    while sequence:
        compressed, count = code_word(sequence)
        sequence = sequence[count:]
        data_out += compressed

    return data_out

def decode_word(word):
    mask = int(b'11110000', 2)
    
    cnt = bytearray(word[3])[0] >> 4
    size = PAYLOAD_SIZE / cnt 
    
    binary_data = unpack('i', word)[0] #bytearray(word)
    res = []
    mask = int('1' * int(size), 2)
    for i in range(cnt):
        res.append(binary_data & mask)
        binary_data = binary_data >> size

    return filter(lambda x: x != 0, res)

def decode(data_in):
    size = len(data_in) / 4
    data_out = []

    for i in range(size):
        data_out += decode_word(data_in[i * 4: (i + 1) * 4])

    return data_out

a = range(1, 30)
print a == decode(code(a))
