# source : https://www.acmicpc.net/problem/10219
# ad hoc

# input
for _ in range(int(input())):
    # input
    h, w = map(int, input().split())

    grill = [list(input()) for _ in range(h)]

    for li in grill:
        for s in reversed(li):
            print(s, end='')
            
        print()