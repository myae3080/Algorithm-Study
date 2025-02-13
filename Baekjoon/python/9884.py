# source : https://www.acmicpc.net/problem/9884

def main():
    # input
    A, B = map(int, input().split())
    
    while A != B:
        if A > B:
            A = A - B
        else:
            B = B - A
    
    print(A)

if __name__ == '__main__':
    main()