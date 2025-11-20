# source : https://www.acmicpc.net/problem/34323

def main():
    # input
    N, M, S = map(int, input().split())

    n_percent = S * (100 - N) * (M + 1) // 100
    plus_one = S * M
    
    print(min(n_percent, plus_one))

if __name__ == '__main__':
    main()