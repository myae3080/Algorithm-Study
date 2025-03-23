# source : https://www.acmicpc.net/problem/6190

def main():
    # input
    N = int(input())
    
    score = 0
    while N > 1:
        if N % 2 == 0:
            N //= 2
        else:
            N = (3 * N) + 1
        
        score += 1
    
    print(score)

if __name__ == '__main__':
    main()