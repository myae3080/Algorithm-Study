# source : https://www.acmicpc.net/problem/5176

for _ in range(int(input())):
    # input
    p, m = map(int, input().split())
    seats = [1] * m
    result = 0
    for _ in range(p):
        # input
        seat = int(input()) - 1

        if seats[seat]:
            seats[seat] = 0
        else:
            result += 1
    
    print(result)