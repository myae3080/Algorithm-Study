# source : https://www.acmicpc.net/problem/23375

def main():
    # input
    x, y = map(int, input().split())
    r = int(input())

    print(x - r, y + r)
    print(x + r, y + r)
    print(x + r, y - r)
    print(x - r, y - r)

if __name__ == '__main__':
    main()