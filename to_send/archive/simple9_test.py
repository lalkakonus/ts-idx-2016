# Kononov Sergey BD-21
# Tests for simple9 archive

from simple9 import * 
import random
import time

test = range(1, 10000)
random.shuffle(test)
t1 = time.time()
res = test == decode(code(test))
t2 = time.time()

print 'simple9 archive tests :', res * 'OK' + (1 - res) * 'ERROR'
print '[1, 10000] compressed and decompressed in', t2 - t1, 'sec'
