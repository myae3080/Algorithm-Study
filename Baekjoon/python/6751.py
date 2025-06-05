# source : https://www.acmicpc.net/problem/6751

def main():
    # input
    Y = input()

    while 1:
        Y = str(int(Y) + 1)
        digits = set(list(Y))

        if len(digits) == len(list(Y)):
            print(Y)

            break

if __name__ == '__main__':
    main()