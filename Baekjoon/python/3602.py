# source : https://www.acmicpc.net/problem/3602

def main():
    # input
    b, w = map(int, input().split())

    if max(b, w) == 0:
        print('Impossible')
    else:
        if b == w:
            print(int((b * 2) ** 0.5))
        else:
            print(int((min(b, w) * 2 + 1) ** 0.5))

if __name__ == '__main__':
    main()