# source : https://www.acmicpc.net/problem/23972

def main():
    # input
    k, n = map(int, input().split())
    
    if n == 1:
        print(-1)
        return
    else:
        result = (k * n) // (n - 1) if (k * n) % (n - 1) == 0 else (k * n) // (n - 1) + 1
    
    print(result)

if __name__ == '__main__':
    main()