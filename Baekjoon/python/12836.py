# source : https://www.acmicpc.net/problem/12836

import sys
input = sys.stdin.readline    
    
def main():
    # input
    n, q = map(int, input().split())
    
    book = [0] * (n + 1)
    for _ in range(q):
        # input
        query = list(map(int, input().split()))
        
        if query[0] == 1:
            book[query[1]] += query[2]
        else:
            print(sum(book[query[1]:query[2] + 1]))

if __name__ == '__main__':
    main()