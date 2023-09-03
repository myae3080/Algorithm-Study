# source : https://www.acmicpc.net/problem/14568

def main():
    # input
    n = int(input())

    result = 0
    for t in range(2, n - 1, 2):
        candies = n - t
        for y in range(1, candies):
            if candies - y >= 2 + y:
                result += 1

    print(result)

if __name__ == '__main__':
    main()