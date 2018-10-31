from tree import *

def test(str_expr, set_expr, N = 1000):
    root = parse(str_expr)
    activate_node(root, N)
    pred = set(execute(root)) == set(set_expr)
    print str_expr, ':', 'OK' * pred + 'ERROR' * (1 - pred)

s_a, s_b, s_c = set(a), set(b), set(c)

print '\nTests:'
test('a          ', s_a, N)
test('a | b      ', s_a | s_b, N)
test('a | b | c  ', s_a | s_c | s_b), N
test('a & b      ', s_a & s_b, N)
test('a & b & c  ', s_a & s_c & s_b, N)
test('a & b | c  ', s_a & s_b | s_c, N)
test('a & (b | c)', s_a & (s_b | s_c), N)
test('!a | !c    ', (set(range(1, N + 1)) - s_a) | (set(range(1, N + 1)) - s_c), N)
test('!a & c     ', (set(range(1, N + 1)) - s_a) & s_c, N)
test('!a         ', set(range(1, N + 1)) - s_a, N)
test('a & !a     ', s_a & (set(range(1, N + 1)) - s_a), N)
test('a & (a | b)', s_a & (s_a | s_b), N)
