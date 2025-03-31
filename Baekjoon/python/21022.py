# source : https://www.acmicpc.net/problem/21022

def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A_score = 0
    for i in range(N):
        if A[i] > B[i]:
            A_score += 3
        elif A[i] == B[i]:
            A_score += 1
    
    print(A_score)

if __name__ == '__main__':
    main()