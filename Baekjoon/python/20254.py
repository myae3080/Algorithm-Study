# source : https://www.acmicpc.net/problem/20254

def main():
    #input
    nums = list(map(int, input().split()))
    
    multi = [56, 24, 14, 6]
    
    print(sum([nums[i] * multi[i] for i in range(len(nums))]))
    
if __name__ == '__main__':
    main()
