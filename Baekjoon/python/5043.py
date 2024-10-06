# source : https://www.acmicpc.net/problem/5043

def main():
    # input
    N, b = map(int, input().split())
    
    print('yes' if 2 ** (b + 1) - 1 >= N else 'no')

if __name__ == '__main__':
    main()