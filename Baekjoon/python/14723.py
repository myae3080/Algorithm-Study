# source : https://www.acmicpc.net/problem/14723

def main():
    # input
    N = int(input())

    a, b = 1, 1
    for _ in range(1, N):
        if a == 1:
            a = b + 1
            b = 1
        else:
            a -= 1
            b += 1

    print(a, b)

if __name__ == '__main__':
    main()