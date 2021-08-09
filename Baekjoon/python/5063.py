# source : https://www.acmicpc.net/problem/5063
# math

for _ in range(int(input())):
    # input
    a, b, c = map(int, input().split())

    ad_benefit = b - c

    if a < ad_benefit:
        print('advertise')
    elif a == ad_benefit:
        print('does not matter')
    else:
        print('do not advertise')