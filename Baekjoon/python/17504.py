# source : https://www.acmicpc.net/problem/17504

def main():
    # input
    n = int(input())
    nums = list(map(int, input().split()))[::-1]
    
    a, b = 1, nums[0]
    for num in nums[1:]:
        a, b = b, (b * num) + a
    
    print(b - a, b)

if __name__ == '__main__':
    main()