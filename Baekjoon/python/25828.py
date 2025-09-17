# https://www.acmicpc.net/problem/25828

def main():
    # input
    g, p, t = map(int, input().split())

    individual, gruop = g * p, g + p * t

    if individual > gruop:
        print(2)
    elif individual < gruop:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()