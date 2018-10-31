# Kononov Sergey BD-21
# Test for varbyte archive

from varbyte import *
import time 
import random
   
test = range(1, 10000)
random.shuffle(test)

t1 = time.time()
test_sum = bool(test == decode_array(code_array(test)))
t2 = time.time()

t3 = time.time()
for i in range(1, 10000):
    test_sum |= i == decode(code(i))
t4 = time.time()

print 'varbyte tests :', test_sum * 'OK' + ~test_sum * 'ERROR'
print '[1, 10000] array compressed and decmpressed in', t2 - t1, 'sec'
print '[1, 10000] ints compressed and decmpressed in', t4 - t3, 'sec'
