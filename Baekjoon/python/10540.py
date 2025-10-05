# source : https://www.acmicpc.net/problem/10540

def main():
    x, y = [], []

    # input
    for _ in range(int(input())):
        # input
        X, Y = map(int, input().split())

        x.append(X)
        y.append(Y)
    
    side = max(max(x) - min(x), max(y) - min(y))

    print(side ** 2)

if __name__ == '__main__':
    main()