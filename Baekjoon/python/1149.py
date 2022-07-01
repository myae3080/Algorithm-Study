# source : https://www.acmicpc.net/problem/1149

# input
n = int(input())
rgbs = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    # 현재 집이 빨강
    rgbs[i][0] += min(rgbs[i - 1][1], rgbs[i - 1][2]) 
    # 현재 집이 초록
    rgbs[i][1] += min(rgbs[i - 1][0], rgbs[i - 1][2])
    # 현재 집이 파랑
    rgbs[i][2] += min(rgbs[i - 1][0], rgbs[i - 1][1])

print(min(rgbs[-1]))