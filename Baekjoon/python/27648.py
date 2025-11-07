# source : https://www.acmicpc.net/problem/27648

def main():
    # input
    N, M, K = map(int, input().split())

    result = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            result[i][j] = i + j + 1
    
    if result[-1][-1] <= K:
        print('YES')

        for arr in result:
            print(*arr)
    else:
        print('NO')

if __name__ == '__main__':
    main()