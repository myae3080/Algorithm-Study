# source : https://www.acmicpc.net/problem/23809

def main():
    # input
    n = int(input())
    
    [print('@' * n + '   ' * n + '@' * n) for _ in range(n)]
    [print('@' * n + '  ' * n + '@' * n) for _ in range(n)]
    [print('@@@' * n) for _ in range(n)]
    [print('@' * n + '  ' * n + '@' * n) for _ in range(n)]
    [print('@' * n + '   ' * n + '@' * n) for _ in range(n)]

if __name__ == '__main__':
    main()