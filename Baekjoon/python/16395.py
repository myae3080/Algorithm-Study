# source : https://www.acmicpc.net/problem/16395
# math, dp, combination

pascal_list = [[1], [1, 1]]

# input
n, k = map(int, input().split())

for i in range(2, n):
    row_list = [1]
    [row_list.append(pascal_list[i - 1][j - 1] + pascal_list[i - 1][j]) for j in range(1, i)]
    row_list.append(1)

    pascal_list.append(row_list)

print(pascal_list[n - 1][k - 1])