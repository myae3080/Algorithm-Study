# source : https://www.acmicpc.net/problem/20499

# input
k, d, a = map(int, input().split('/'))

print('hasu') if d == 0 or k + a < d else print('gosu')