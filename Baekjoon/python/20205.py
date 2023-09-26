# source : https://www.acmicpc.net/problem/20205

def main():
    # input
    n, k = map(int, input().split())
    bitmap = [list(input().split()) for _ in range(n)]
    
    for i in range(n):
        for _ in range(k):
            for j in range(n):
                for _ in range(k):
                    print(bitmap[i][j], end=' ')
            print()

if __name__ == '__main__':
    main()