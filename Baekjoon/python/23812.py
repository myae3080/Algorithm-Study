# source : https://www.acmicpc.net/problem/23812

def main():
    # input
    n = int(input())
    
    for i in range(5):
        if i % 2 == 0:
            [print('@' * n + ' ' * n * 3 + '@' * n) for _ in range(n)]
        else:
            [print('@' * n * 5) for _ in range(n)]
    
if __name__ == '__main__':
    main()