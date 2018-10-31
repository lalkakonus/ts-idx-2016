import numpy as np

N = 500
p = 0.5
M = int(N * p)

def make_vec(N):
    rand_mask = np.ones(N)
    rand_mask[np.random.randint(0, N, M)] = 0
    return np.arange(1, N + 1)[rand_mask.astype(bool)]

a = make_vec(N)
b = make_vec(N)
c = make_vec(N)

dic = {'a': list(a),
       'b': list(b),
       'c': list(c)}
# print ' a:', a, '\n b:', b, '\n c:', c, '\n'
