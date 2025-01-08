# source : https://www.acmicpc.net/problem/25177

def main():
    # input
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a += [0] * (M - N)
    b += [0] * (N - M)
    
    result = 0
    for i in range(max(N, M)):
        result = max(result, b[i] - a[i])
    
    print(result)

if __name__ == '__main__':
    main()