# source : https://www.acmicpc.net/problem/19941

def main():
    # input
    N, K = map(int, input().split())
    locations = list(input())

    result = 0
    eaten = [0] * N
    for i in range(N):
        if locations[i] == 'P':
            for j in range(max(i - K, 0), min(i + K + 1, N)):
                if locations[j] == 'H' and eaten[j] == 0:
                    result += 1
                    eaten[j] = 1

                    break

    print(result)

if __name__ == '__main__':
    main()