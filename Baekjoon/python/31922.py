# source : https://www.acmicpc.net/problem/31922

def main():
    # input
    A, P, C = map(int, input().split())

    print(max(A + C, P))

if __name__ == '__main__':
    main()