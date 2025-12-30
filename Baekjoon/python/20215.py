# source : https://www.acmicpc.net/problem/20215

def main():
    # input
    w, h = map(int, input().split())

    print("{:.6f}".format((w + h) - ((w ** 2 + h ** 2) ** 0.5)))

if __name__ == '__main__':
    main()