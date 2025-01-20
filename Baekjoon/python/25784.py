# source : https://www.acmicpc.net/problem/25784

def main():
    # input
    nums = sorted(list(map(int, input().split())))
    
    if nums[0] + nums[1] == nums[2]:
        print(1)
    elif nums[0] * nums[1] == nums[2]:
        print(2)
    else:
        print(3)

if __name__ == '__main__':
    main()