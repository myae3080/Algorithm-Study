# source : https://www.acmicpc.net/problem/3208

def main():
    # input
    M, N = map(int, input().split())

    if M > N:
        print((N - 1) * 2 + 1)
    else:
        print((M - 1) * 2)

if __name__ == '__main__':
    main()