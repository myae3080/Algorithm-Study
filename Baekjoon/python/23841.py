# source : https://www.acmicpc.net/problem/23841

# input
n, m = map(int, input().split())
painting = [list(input()) for _ in range(n)]

for paint in painting:
    for i, v in enumerate(paint):
        if v != '.' and paint[m - i - 1] == '.':
            paint[m - i - 1] = v

[print(''.join(paint)) for paint in painting]