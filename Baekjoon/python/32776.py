# source : https://www.acmicpc.net/problem/32776

def main():
    # input
    s = int(input())
    mA, f, mB = map(int, input().split())

    if s <= 240 or s <= mA + f + mB:
        print('high speed rail')
    else:
        print('flight')

if __name__ == '__main__':
    main()