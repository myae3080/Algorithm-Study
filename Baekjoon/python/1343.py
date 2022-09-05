# source : https://www.acmicpc.net/problem/1343

# input
board = input()

board = board.replace('XXXX', 'AAAA').replace('XX', 'BB')
print(-1) if board.count('X') else print(board)