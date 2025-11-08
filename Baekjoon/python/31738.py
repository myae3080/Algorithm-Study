# source : https://www.acmicpc.net/problem/31738

def main():
    # input
    N, M = map(int, input().split())

    result = 1
    for n in range(2, N + 1):
        result *= n
        result %= M
        
        if result == 0:
            break
    
    print(result)

if __name__ == '__main__':
    main()