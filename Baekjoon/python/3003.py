# source : https://www.acmicpc.net/problem/3003
# math

chess_pieces = [1, 1, 2, 2, 2, 8]
result = [0] * 6

# input
input_pieces = list(map(int, input().split()))

for i in range(len(chess_pieces)):
    result[i] = str(chess_pieces[i] - input_pieces[i])

print(' '.join(result))