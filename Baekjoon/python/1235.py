# source : https://www.acmicpc.net/problem/1235

# input
n = int(input())
ids = [input() for _ in range(n)]

k = 1
length = len(ids[0])
while 1:
    uniques = set([ids[i][length - k:] for i in range(n)])
    
    if len(uniques) == n:
        break

    k += 1
    
print(k)