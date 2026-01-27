# source : https://www.acmicpc.net/problem/8674

def main():
    # input
    a, b = map(int, input().split())

    if a % 2 == 0 or b % 2 == 0:
        print(0)
    else:
        print(min(a, b))

if __name__ == '__main__':
    main()