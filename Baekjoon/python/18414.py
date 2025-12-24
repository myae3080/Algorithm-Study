# source : https://www.acmicpc.net/problem/18414

def main():
    # input
    X, L, R = map(int, input().split())

    if X < L:
        print(L)
    elif X > R:
        print(R)
    else:
        print(X)

if __name__ == '__main__':
    main()