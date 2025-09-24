# source : https://www.acmicpc.net/problem/19945

def main():
    # input
    n = int(input())

    if n >= 0:
        print(len(bin(n)[2:]))
    else:
        print(32)

if __name__ == '__main__':
    main()