# source : https://www.acmicpc.net/problem/17202
# dp

a, b = input(), input()

ab = ''

for i in range(int(len(a))):
    ab += (a[i] + b[i])

while len(ab) > 2:
    temp = ''
    
    for i in range(len(ab) - 1):
        temp += str(int(ab[i]) + int(ab[i + 1]))[-1]
    
    ab = temp
    
print(ab)