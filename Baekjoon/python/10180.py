# source : https://www.acmicpc.net/problem/10180

def main():
    # input
    T = int(input())
    
    for _ in range(T):
        # input
        N, D = map(int, input().split())
        
        result = 0
        for __ in range(N):
            # input
            v, f, c = map(int, input().split())
            
            if f >= (D / v) * c:
                result += 1
        
        print(result)

if __name__ == '__main__':
    main()