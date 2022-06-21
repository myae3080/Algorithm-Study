# source : https://www.acmicpc.net/problem/1855

# input
col = int(input())
encrypted = input()

table = [encrypted[i - col: i] for i in range(col, len(encrypted) + 1, col)]
result = ''

for i in range(len(table)):
    if i % 2 == 1:
        table[i] = table[i][::-1]
        
for i in range(len(table[0])):
    for j in range(len(table)):
        result += table[j][i]
        
print(result)