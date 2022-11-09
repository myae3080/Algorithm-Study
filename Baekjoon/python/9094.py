# source : https://www.acmicpc.net/problem/9094

# PyPy3
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    # input
    n, m = map(int, input().split())
    
    result = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n):
            if (i ** 2 + j ** 2 + m) % (i * j) == 0:
                result += 1
                
    print(result)