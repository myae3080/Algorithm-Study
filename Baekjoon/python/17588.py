# source : https://www.acmicpc.net/problem/17588

def main():
    # input
    n = int(input())
    nums = [int(input()) for _ in range(n)]

    missing_nums = []
    for num in range(1, nums[-1]):
        if num not in nums:
            missing_nums.append(str(num))

    print('good job' if not missing_nums else '\n'.join(missing_nums))

if __name__ == '__main__':
    main()