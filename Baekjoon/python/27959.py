# source : https://www.acmicpc.net/problem/27959

def main():
    # input
    n, m = map(int, input().split())

    print('Yes' if n * 100 >= m else 'No')

if __name__ == '__main__':
    main()