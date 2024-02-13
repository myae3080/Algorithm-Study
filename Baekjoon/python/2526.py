# source : https://www.acmicpc.net/problem/2526

def main():
    # input
    n, p = map(int, input().split())
    
    nums = [n]
    num = n
    while 1:
        num = num * n % p
        
        if num in nums:
            print(len(nums) - nums.index(num))
            break
        
        nums.append(num)

if __name__ == '__main__':
    main()