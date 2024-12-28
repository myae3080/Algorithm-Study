# source : https://www.acmicpc.net/problem/9306

def main():
    # input
    for i in range(1, int(input()) + 1):
        # input
        first, last = input(), input()

        print('Case %d: %s, %s' % (i, last, first))

if __name__ == '__main__':
    main()