# dp

# input
n = int(input())
triangle_list = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    length = len(triangle_list[i])

    for j in range(length):
        # 배열 첫번째 요소
        if j == 0:
            triangle_list[i][j] += triangle_list[i - 1][j]
        # 배열 마지막 요소
        elif j == length - 1:
            triangle_list[i][j] += triangle_list[i - 1][j - 1]
        else:
            triangle_list[i][j] += max(triangle_list[i - 1][j - 1], triangle_list[i - 1][j])

print(max(triangle_list[n - 1]))