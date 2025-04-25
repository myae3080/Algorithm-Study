# source : https://www.acmicpc.net/problem/33541

def main():
    # input
    X = int(input())
    
    while X < 9999:
        X += 1
        fore, back = int(str(X)[:2]), int(str(X)[2:])
        
        if (fore + back) ** 2 == int(X):
            print(X)
            
            return
        
    print(-1)

if __name__ == '__main__':
    main()