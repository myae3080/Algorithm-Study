# source : https://www.acmicpc.net/problem/24228

def main():
    # input
    N, R = map(int, input().split())

    print(N - 1 + (R * 2))

if __name__ == '__main__':
    main()