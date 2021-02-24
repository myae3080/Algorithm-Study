import collections

# deque의 경우, FIFO, LILO 둘 다 구현할 수 있는 자료구조.
# 
test_deque = collections.deque(['A', 'B', 'C'])
test_deque2 = collections.deque(['A', 'B', 'C'])
test_deque.append('D')

print(test_deque)

test_deque.appendleft('AA')

print(test_deque)

test_deque.append('ef')
test_deque2.extend('ef')

print('test_deque : ', test_deque)
print('test_deque2 : ', test_deque2)
