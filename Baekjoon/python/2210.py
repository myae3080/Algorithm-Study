# source : https://www.acmicpc.net/problem/2210

# input
board = [list(input().split()) for _ in range(5)]

def dfs(number: str, coordinate: tuple, numbers: set):
    x, y = coordinate
    number += board[x][y]

    if len(number) == 6:
        numbers.add(number)
    else:
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = x + direction[0], y + direction[1]

            if 5 > next_x >= 0 and 5 > next_y >= 0:
                dfs(number, (next_x, next_y), numbers)

numbers = set()
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(5):
    for j in range(5):
        dfs('', (i, j), numbers)

print(len(numbers))