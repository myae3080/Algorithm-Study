# source : https://www.acmicpc.net/problem/5566

# input
n, m = map(int, input().split())
board = [int(input()) for _ in range(n)]
dice = [int(input()) for _ in range(m)]

step = 1

for i in range(1, m + 1):
    step += dice[i - 1]
    
    if step >= n:
        print(i)
        break
    
    step += board[step - 1]

    if step >= n:
        print(i)
        break