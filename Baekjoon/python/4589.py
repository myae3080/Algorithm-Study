# source : https://www.acmicpc.net/problem/4589

def main():
    print('Gnomes:')
    
    for _ in range(int(input())):
        # input
        nums = list(map(int, input().split()))

        if nums == sorted(nums) or nums == sorted(nums, reverse=True):
            print('Ordered')
        else:
            print('Unordered')
        
if __name__ == '__main__':
    main()