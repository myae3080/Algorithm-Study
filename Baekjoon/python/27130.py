# source : https://www.acmicpc.net/problem/27130

def main():
    # input
    a, b = input(), input()

    print(a)
    print(b)

    for i in range(len(b) - 1, -1, -1):
        print(int(a) * int(b[i]))

    print(int(a) * int(b))

if __name__ == '__main__':
    main()