# source : https://www.acmicpc.net/problem/18141

from itertools import permutations

def main():
    # input
    n = int(input())
    ints = list(map(int, input().split()))
    
    for nums in list(permutations(ints, 3)):
        curr = (nums[0] - nums[1]) / nums[2]
        if curr != int(curr):
            print('no')
            return
    
    print('yes')

if __name__ == '__main__':
    main()