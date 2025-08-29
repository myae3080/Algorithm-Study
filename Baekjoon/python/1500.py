# source : https://www.acmicpc.net/problem/1500

def main():
    # input
    S, K = map(int, input().split())

    rest = S % K
    nums = [S // K for _ in range(K)]
    for i in range(rest):
        nums[i] += 1
    
    result = 1
    for num in nums:
        result *= num
    
    print(result)

if __name__ == '__main__':
    main()