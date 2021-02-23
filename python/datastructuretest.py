import collections

test_deque = collections.deque(['A', 'B', 'C'])
test_deque.append('D')

print(test_deque)

test_deque.appendleft('AA')

print(test_deque)