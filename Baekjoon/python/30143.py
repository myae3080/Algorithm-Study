# source : https://www.acmicpc.net/problem/30143

def main():
    # input
    for _ in range(int(input())):
        # input
        N, A, D = map(int, input().split())
        
        print((N * (2 * A + (N - 1) * D)) // 2)

if __name__ == '__main__':
    main()