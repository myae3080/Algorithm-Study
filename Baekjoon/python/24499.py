# source : https://www.acmicpc.net/problem/24499

def main():
    # input
    N, K = map(int, input().split())
    apple_pies = list(map(int, input().split()))

    window = sum(apple_pies[0:K])
    result = window
    for i in range(1, N):
        out_idx = (i - 1) % N
        in_idx = (i + K - 1) % N
        window += (apple_pies[in_idx] - apple_pies[out_idx])

        result = max(result, window)
    
    print(result)

if __name__ == '__main__':
    main()