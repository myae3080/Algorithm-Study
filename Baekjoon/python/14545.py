# source : https://www.acmicpc.net/problem/14545

def main():
    # input
    n = int(input())

    squares = [i * i for i in range(1, 1000001)]
    for _ in range(n):
        # input
        print(sum(squares[:int(input())]))

if __name__ == '__main__':
    main()