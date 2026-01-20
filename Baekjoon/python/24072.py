# source : https://www.acmicpc.net/problem/24072

def main():
    # input
    A, B, C = map(int, input().split())

    if A <= C < B:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()