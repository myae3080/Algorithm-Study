#  source : https://www.acmicpc.net/problem/11637

import sys
input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        candidates = [int(input()) for __ in range(int(input()))]
        
        max_votes = max(candidates)
        
        if candidates.count(max_votes) == 1:
            candidate = candidates.index(max_votes) + 1
            print('majority winner %d' % candidate if max_votes > sum(candidates) // 2 else 'minority winner %d' % candidate)
        else:
            print('no winner')
    
if __name__ == '__main__':
    main()