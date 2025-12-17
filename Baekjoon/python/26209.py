# source : https://www.acmicpc.net/problem/26209

def main():
    # input
    bits = list(map(int, input().split()))

    print('F' if bits.count(9) > 0 else 'S')

if __name__ == '__main__':
    main()