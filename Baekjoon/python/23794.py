# source : https://www.acmicpc.net/problem/23794

def main():
    # input
    n = int(input())
    
    print('@' * (n + 2))
    [print('@' + ' ' * (n) + '@') for _ in range(n)]
    print('@' * (n + 2))

if __name__ == '__main__':
    main()