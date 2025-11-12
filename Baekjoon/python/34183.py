# source : https://www.acmicpc.net/problem/34183

def main():
    # input
    N, M, A, B = map(int, input().split())

    target_chairs = N * 3
    if M >= target_chairs:
        print(0)
    else:
        print((target_chairs - M) * A + B)

if __name__ == '__main__':
    main()