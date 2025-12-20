# source : https://www.acmicpc.net/problem/34529

def main():
    # input
    X, Y, Z = map(int, input().split())
    U, V, W = map(int, input().split())

    print(((U // 100) * X) + ((V // 50) * Y) + ((W // 20) * Z))

if __name__ == '__main__':
    main()