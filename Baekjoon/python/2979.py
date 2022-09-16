# source : https://www.acmicpc.net/problem/2979

# input
fee1, fee2, fee3 = map(int, input().split())

times = [0] * 101
for _ in range(3):
    # input
    start, end = map(int, input().split())

    for i in range(start + 1, end + 1):
        times[i] += 1
        
result = 0
for i in range(1, 101):
    t = times[i]
    
    if t == 1:
        result += t * fee1
    elif t == 2:
        result += t * fee2
    else:
        result += t * fee3
        
print(result)