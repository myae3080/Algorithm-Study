# source : https://www.acmicpc.net/problem/23804

def main():
    # input
    n = int(input())
    
    pattern1, pattern2 = '@@@@@', '@'
    
    [print(pattern1 * n) for i in range(n)]
    [print(pattern2 * n) for i in range(n * 3)]
    [print(pattern1 * n) for i in range(n)]
    
if __name__ == '__main__':
    main()