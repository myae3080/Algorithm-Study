# source : https://www.acmicpc.net/problem/2810

def main():
    # input
    n = int(input())
    seats = input()

    couples = seats.count('LL')

    print(n - couples + 1 if couples > 0 else n)

if __name__ == '__main__':
    main()