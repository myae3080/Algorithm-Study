# source : https://www.acmicpc.net/problem/32902

def main():
    # input
    k, n = map(int, input().split())

    print(n + 1, k * n + 1)

if __name__ == '__main__':
    main()