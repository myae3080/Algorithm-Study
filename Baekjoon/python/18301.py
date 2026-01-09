# source : https://www.acmicpc.net/problem/18301

def main():
    # input
    n1, n2, n12 = map(int, input().split())

    print(((n1 + 1) * (n2 + 1) // (n12 + 1)) - 1)

if __name__ == '__main__':
    main()