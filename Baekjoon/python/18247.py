# source : https://www.acmicpc.net/problem/18247

def main():
    # input
    t = int(input())

    for _ in range(t):
        # input
        n, m = map(int, input().split())

        if n < 12 or m < 4:
            print(-1)
        else:
            print((11 * m) + 4)

if __name__ == '__main__':
    main()