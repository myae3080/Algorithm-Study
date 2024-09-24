# source : https://www.acmicpc.net/problem/14648

import sys
input = sys.stdin.readline

def main():
    # input
    n, q = map(int, input().split())
    nums = list(map(int, input().split()))
    
    for _ in range(q):
        # input
        query = list(map(int, input().split()))
        
        if query[0] == 1:
            print(sum(nums[query[1] - 1:query[2]]))
            
            nums[query[1] - 1], nums[query[2] - 1] = nums[query[2] - 1], nums[query[1] - 1]
        else:
            print(sum(nums[query[1] - 1:query[2]]) - sum(nums[query[3] - 1:query[4]]))

if __name__ == '__main__':
    main()