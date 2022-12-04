# source : https://www.acmicpc.net/problem/16431

# input
bx, by = map(int, input().split())
dx, dy = map(int, input().split())
jx, jy = map(int, input().split())

bessie = max(abs(jx - bx), abs(jy - by))
daisy = abs(jx - dx) + abs(jy - dy)

print('tie') if bessie == daisy else print('daisy') if bessie > daisy else print('bessie')