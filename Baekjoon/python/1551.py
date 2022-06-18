# source : https://www.acmicpc.net/problem/1551

# input
n, k = map(int, input().split())
sequence = list(map(int, input().split(',')))

'''
    time complexity : O(n)
    space complexity : O(1)
'''
while k:
    sequence = [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]
    k -= 1
    
print(','.join([str(n) for n in sequence]))