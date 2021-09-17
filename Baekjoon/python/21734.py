# source : https://www.acmicpc.net/problem/21734
# string

# input
for c in input():
    for _ in range(sum(list(map(int, str(ord(c)))))):
        print(c, end='')
    
    print()