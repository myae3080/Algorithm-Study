# source : https://www.acmicpc.net/problem/15995

def main():
    # input
    a, m = map(int, input().split())

    for n in range(1, 10001):
        if (a * n) % m == 1:
            print(n)
            break

if __name__ == '__main__':
    main()