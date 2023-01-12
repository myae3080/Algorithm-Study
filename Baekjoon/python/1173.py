# source : https://www.acmicpc.net/problem/1173

# input
N, m, M, T, R = map(int, input().split())

result, ex_minute = 0, 0

if m + T > M:
    print(-1)
else:
    pulse = m
    while ex_minute < N:
        result += 1
        
        if pulse + T <= M:
            pulse += T
            ex_minute += 1
        else:
            pulse = max(pulse - R, m)
            
    print(result if ex_minute == N else -1)