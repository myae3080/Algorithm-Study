# source : https://www.acmicpc.net/problem/30019

import sys 
input = sys.stdin.readline

def main():
    # input
    n, m = map(int, input().split())
    
    reservation = {}
    for num in range(1, n + 1):
        reservation[num] = []
        
    for _ in range(m):
        # input
        k, s, e = map(int, input().split())
        
        if len(reservation[k]) > 0:
            if max(reservation[k]) <= s or min(reservation[k]) >= e:
                reservation[k][0] = min(reservation[k][0], s)
                reservation[k][1] = max(reservation[k][1], e)
                
                print('YES')
            else:
                print('NO')
        else:
            reservation[k].append(s)
            reservation[k].append(e)
            
            print('YES')

if __name__ == '__main__':
    main()