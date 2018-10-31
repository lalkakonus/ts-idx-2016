# Kononov Sergey BD-21

from struct import pack, unpack

BITS = [1, 2, 3, 4, 5, 7, 9, 14, 28]
BITS_LEN = len(BITS)
BORDER = [2 ** x for x in BITS]
PAYLOAD_SIZE = 28

def define_size(value):
    global BITS, BITS_LEN, BORDER

    for idx in range(BITS_LEN):
        if value < BORDER[idx]:
            return BITS[idx]
    return None

def define_count(sequence):
    global PAYLOAD_SIZE
    cnt = 0
    maximum = 0
    
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

    for i, x in enumerate(BITS): 
        if x > cnt:
            round_cnt = BITS[i - 1]
            break
    size = PAYLOAD_SIZE / round_cnt

    compressed = round_cnt << PAYLOAD_SIZE
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
    cnt = bytearray(word[3])[0] >> 4
    size = PAYLOAD_SIZE / cnt 
    mask = int('1' * size, 2)
    
    result = []
    binary_data = unpack('i', word)[0]
    for i in range(cnt):
        result.append(binary_data & mask)
        binary_data = binary_data >> size

    return filter(lambda x: x != 0, result)

def decode(data_in):
    size = len(data_in) / 4
    data_out = []

    for i in range(size):
        data_out += decode_word(data_in[i * 4: (i + 1) * 4])

    return data_out
