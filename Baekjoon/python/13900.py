# source : https://www.acmicpc.net/problem/13900

def main():
    # input
    N = int(input())
    nums = sorted(list(map(int, input().split())))

    ''' solution
        2 3 3
        (2, 3) (2, 3)
        (3, 3)
    '''
    result = 0
    pre_sum = 0
    for i in range(N):
        result += nums[i] * pre_sum
        pre_sum += nums[i]

    print(result)

if __name__ == '__main__':
    main()