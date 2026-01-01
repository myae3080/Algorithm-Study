# source : https://www.acmicpc.net/problem/34009

def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))

    print('Alice' if N % 2 == 0 else 'Bob')

if __name__ == '__main__':
    main()