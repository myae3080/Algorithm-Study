# source : https://www.acmicpc.net/problem/10395

def main():
    # input
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    for i in range(len(X)):
        if X[i] == Y[i]:
            print('N')

            return 
    
    print('Y')

if __name__ == '__main__':
    main()