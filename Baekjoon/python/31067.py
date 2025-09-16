# source : https://www.acmicpc.net/problem/31067

def main():
    # input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    result = 0
    for i in range(1, N):
        if A[i - 1] >= A[i]:
            A[i] += K
        else:
            continue
        
        if A[i - 1] >= A[i]:
            result = -1

            break
        else:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()