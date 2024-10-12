# source : https://www.acmicpc.net/problem/31668

def main():
    # input
    N, M, K = int(input()), int(input()), int(input())

    print((M // N) * K)

if __name__ == '__main__':
    main()