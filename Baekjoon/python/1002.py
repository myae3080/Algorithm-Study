# source : https://www.acmicpc.net/problem/1002

import math

for _ in range(int(input())):
    # input
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    d = math.sqrt(((x1 - x2) ** 2 + (y1 - y2) ** 2))
    
    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        r_sum, r_diff = r1 + r2, abs(r1 - r2)
        
        if d > r_sum:
            print(0)
        elif d == r_sum:
            print(1)
        # 두 개의 교점
        elif r_diff < d < r_sum:
            print(2)
        # 내접 시, 한 개의 교점
        elif d == r_diff:
            print(1)
        else:
            print(0)