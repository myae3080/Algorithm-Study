# source : https://www.acmicpc.net/problem/32775

def main():
    # input
    s, f = int(input()), int(input())

    print('high speed rail' if s <= f else 'flight')

if __name__ == '__main__':
    main()