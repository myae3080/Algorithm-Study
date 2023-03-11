# source : https://www.acmicpc.net/problem/16204

def main():
    # input
    n, m, k = map(int, input().split())

    print(min(m, k) + min(n - m, n - k))

if __name__ == '__main__':
    main()