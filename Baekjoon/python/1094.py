# source : https://www.acmicpc.net/problem/1094

def main():
    # input
    x = int(input())

    print(bin(x)[2:].count('1'))

if __name__ == '__main__':
    main()
