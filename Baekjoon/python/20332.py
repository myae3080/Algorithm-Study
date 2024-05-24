# source : https://www.acmicpc.net/problem/20332

def main():
    # input
    n = int(input())
    contests = list(map(int, input().split()))

    print('yes' if sum(contests) % 3 == 0 else 'no')

if __name__ == '__main__':
    main()