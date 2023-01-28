# source : https://www.acmicpc.net/problem/9501

for _ in range(int(input())):
    # input
    n, d = map(int, input().split())
    
    result = 0
    for _ in range(n):
        # input
        v, f, c = map(int, input().split())
        
        if (f / c) * v >= d:
            result += 1

    print(result)