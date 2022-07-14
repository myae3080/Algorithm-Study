# source : https://www.acmicpc.net/problem/5988

for _ in range(int(input())):
    # input
    k = int(input())
    
    print('even') if k % 2 == 0 else print('odd')