# brute force

# input
n, m = map(int, input().split())

chessboard = [list(input()) for i in range(n)]

horizontal = n - 8
vertical = m - 8
fix_min = 64

for i in range(horizontal + 1):
    for j in range(vertical + 1):
        start = chessboard[i][j]

        b_count = 0
        w_count = 0

        # B
        # 가로 먼저 탐색 후, 세로로
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                square = chessboard[k][l]

                if l % 2 == 0:
                    if k % 2 == 0 and square == 'W':
                        b_count += 1
                    if k % 2 == 1 and square == 'B':
                        b_count += 1
                else:
                    if k % 2 == 0 and square == 'B':
                        b_count += 1
                    if k % 2 == 1 and square == 'W':
                        b_count += 1

        # W
        # 가로 먼저 탐색 후, 세로로
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                square = chessboard[k][l]

                if l % 2 == 0:
                    if k % 2 == 0 and square == 'B':
                        w_count += 1
                    if k % 2 == 1 and square == 'W':
                        w_count += 1
                else:
                    if k % 2 == 0 and square == 'W':
                        w_count += 1
                    if k % 2 == 1 and square == 'B':
                        w_count += 1

        fix_min = min(b_count, w_count, fix_min)

print(fix_min)