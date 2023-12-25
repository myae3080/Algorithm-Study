# source : https://www.acmicpc.net/problem/15734

def main():
    # input
    L, R, A = map(int, input().split())
    
    while A > 0:
        if L <= R:
            L += 1
        else:
            R += 1
        
        A -= 1
    
    print(min(L, R) * 2)
    
if __name__ == '__main__':
    main()