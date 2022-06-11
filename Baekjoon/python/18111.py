# source : https://www.acmicpc.net/problem/18111
# brute force

# python3는 시간 초과, PyPy3는 통과

import sys

input = sys.stdin.readline

# input
n, m, b = map(int, input().split())

blocks = [list(map(int, input().split())) for _ in range(n)]
min_sec, max_height = sys.maxsize, 0

for h in range(257):
    max_block, min_block = 0, 0
    
    for i in range(n):
        for j in range(m):
            block_height = blocks[i][j]
            
            # 땅을 깎는 개수
            if block_height > h:
                max_block += block_height - h
            # 땅을 쌓는 개수
            else:
                min_block += h - block_height

    # max_block + b가 최종적인 인벤의 block 수이고, 그 수가 쌓아야 하는 개수보다 크거나 같아야 땅을 고르게 할 수 있음.
    if max_block + b >= min_block:
        spent_sec = (max_block * 2) + min_block
        
        if min(spent_sec, min_sec) == spent_sec:
            max_height = h
            min_sec = spent_sec
            
print(min_sec, max_height)