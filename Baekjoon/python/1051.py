# source : https://www.acmicpc.net/problem/1051

def main():
    # input
    N, M = map(int, input().split())
    nums = [input() for _ in range(N)]
    
    max_square = 1
    for i in range(N):
        for j in range(M):
            for k in range(j + 1, M):
                length = k - j
                if i + length >= N:
                    continue
                
                if nums[i][j] == nums[i][k] == nums[i + length][j] == nums[i + length][k]:
                    max_square = max(max_square, (length + 1) ** 2)
    
    print(max_square)

if __name__ == '__main__':
    main()