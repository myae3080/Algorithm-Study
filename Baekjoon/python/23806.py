# source : https://www.acmicpc.net/problem/23806

def main():
    # input
    n = int(input())
    
    [print('@@@@@' * n) for _ in range(n)]
    [print('@' * n + '   ' * n + '@' * n) for _ in range(n * 3)]
    [print('@@@@@' * n) for _ in range(n)]
    
if __name__ == '__main__':
    main()