# source : https://www.acmicpc.net/problem/15953
# math

def festival1(rank):
    if rank == 1:
        return 5000000
    elif rank >= 2 and rank < 4:
        return 3000000
    elif rank >= 4 and rank < 7:
        return 2000000
    elif rank >= 7 and rank < 11:
        return 500000
    elif rank >= 11 and rank < 16:
        return 300000
    elif rank >= 16 and rank < 22:
        return 100000
    else:
        return 0

def festival2(rank):
    if rank == 1:
        return 5120000
    elif rank >= 2 and rank < 4:
        return 2560000
    elif rank >= 4 and rank < 8:
        return 1280000
    elif rank >= 8 and rank < 16:
        return 640000
    elif rank >= 16 and rank < 32:
        return 320000
    else:
        return 0

for _ in range(int(input())):
    # input
    a, b = map(int, input().split())

    print(festival1(a) + festival2(b))