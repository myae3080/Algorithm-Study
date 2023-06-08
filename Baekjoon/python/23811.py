# source : https://www.acmicpc.net/problem/23811

def main():
    # input
    n = int(input())
    
    for i in range(5):
        if i % 2 == 0:
            [print('@@@@@' * n) for _ in range(n)]
        else:
            [print('@' * n) for _ in range(n)]

if __name__ == '__main__':
    main()