# source : https://www.acmicpc.net/problem/6975

import sys
input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        n = int(input())
        
        total_sum = sum([num for num in range(1, n) if n % num == 0])
        
        if total_sum < n:
            status = 'a deficient'
        elif total_sum == n:
            status = 'a perfect'
        else:
            status = 'an abundant'
        
        print('%d is %s number.' % (n, status))
        print()

if __name__ == '__main__':
    main()