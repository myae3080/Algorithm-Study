# source : https://www.acmicpc.net/problem/9723

def main():
    # input
    for i in range(int(input())):
        # input
        sides = sorted(list(map(int, input().split())))
        
        if sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
            print('Case #%d: YES' % (i + 1))
        else:
            print('Case #%d: NO' % (i + 1))

if __name__ == '__main__':
    main()