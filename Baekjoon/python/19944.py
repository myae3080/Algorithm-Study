# source : https://www.acmicpc.net/problem/19944

# input
n, m = map(int, input().split())

if m <= n:
    if m == 1 or m == 2:
        print('NEWBIE!')
    else:
        print('OLDBIE!')
else:
    print('TLE!')