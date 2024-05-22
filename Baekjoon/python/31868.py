# source : https://www.acmicpc.net/problem/31868

def main():
    # input
    n, k = map(int, input().split())
    
    print(k // (2 ** (n - 1)))

if __name__ == '__main__':
    main()