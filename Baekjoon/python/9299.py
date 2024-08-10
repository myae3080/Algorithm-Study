# source : https://www.acmicpc.net/problem/9299

import sys
input = sys.stdin.readline

def main():
    # input
    for i in range(1, int(input()) + 1):
        # input
        nums = list(map(int, input().split()))
        
        degree = nums[0]
        result = []
        for n in nums[1:-1]:
            result.append(str(n * degree))
            degree -= 1
        
        print('Case %d: %d %s' % (i, nums[0] - 1, ' '.join(result)))

if __name__ == '__main__':
    main()