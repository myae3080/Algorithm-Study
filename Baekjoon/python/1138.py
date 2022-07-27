# source : https://www.acmicpc.net/problem/1138

# input
n = int(input())
line = list(map(int, input().split()))

result = [0] * n

for i in range(n):
    zeroes, prev = 0, line[i]
    
    for j in range(n):
        if result[j] == 0:
            if zeroes == prev:
                result[j] = str(i + 1)
                break
            else:
                zeroes += 1
            
print(' '.join(result))