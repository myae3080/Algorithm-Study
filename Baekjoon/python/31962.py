# source : https://www.acmicpc.net/problem/31962

def main():
    # input
    N, X = map(int, input().split())
    
    result = 0
    for _ in range(N):
        # input
        S, T = map(int, input().split())
        
        if S + T <= X:
            result = max(result, S)
    
    print(result if result > 0 else -1)

if __name__ == '__main__':
    main()