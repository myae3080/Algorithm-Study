# source : https://www.acmicpc.net/problem/18353

def main():
    # input
    N = int(input())
    soldiers = list(map(int, input().split()))
    
    dp = [1] * N
    for i in range(N):
        for j in range(i):
            if soldiers[i] < soldiers[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    print(N - max(dp))

if __name__ == '__main__':
    main()