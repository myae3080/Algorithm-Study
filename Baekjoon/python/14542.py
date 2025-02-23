# source : https://www.acmicpc.net/problem/14542

import sys

input = sys.stdin.readline

def main():
    case = 0
    while 1:
        # input
        n = int(input())
        
        if n == 0:
            break
    
        case += 1
        result = 0
        for i in range(1, n + 1):
            # input
            nums = list(map(int, input().split()))
            
            if i == 1:
                result += nums[0]
            elif i == n:
                result += sum(nums)
            else:
                result += (nums[0] + nums[-1])
        
        print('Case #%d:%d' % (case, result))

if __name__ == '__main__':
    main()