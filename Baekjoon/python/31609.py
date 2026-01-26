# source : https://www.acmicpc.net/problem/31609

def main():
    # input
    N = int(input())
    nums = sorted(list(map(int, input().split())))

    prev = None
    for num in nums:
        if num != prev:
            print(num)

            prev = num

if __name__ == '__main__':
    main()