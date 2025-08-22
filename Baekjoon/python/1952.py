# source : https://www.acmicpc.net/problem/1952

def main():
    # input
    M, N = map(int, input().split())

    if M > N:
        print(N * 2 - 1)
    else:
        print(M * 2 - 2)

if __name__ == '__main__':
    main()