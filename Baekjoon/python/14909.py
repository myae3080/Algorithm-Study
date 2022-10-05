# source : https://www.acmicpc.net/problem/14909

result = 0

# input
for num in list(map(int, input().split())):
    if num > 0:
        result += 1
        
print(result)