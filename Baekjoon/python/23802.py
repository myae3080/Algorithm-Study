# source : https://www.acmicpc.net/problem/23802

def main():
    # input
    n = int(input())
    
    [print('@@@@@' * n) for _ in range(n)]
    [print('@' * n) for _ in range(n * 4)]
        
if __name__ == '__main__':
    main()