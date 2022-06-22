# source : https://www.acmicpc.net/problem/5430

'''
    R / 0 / [] case의 경우 출력이 error가 아닌 [] 이어야 하는 반례를 고려해야 함.
'''
import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    # input
    p, n = input().rstrip(), int(input())
    deq = deque(input().rstrip()[1:-1].split(','))
    
    reverse_flag = 0
    
    if n == 0:
        deq = []
    
    for fn in p:
        if fn == 'R':
            reverse_flag += 1
        else:
            if deq:
                if reverse_flag % 2 == 1:
                    deq.pop()
                else:
                    deq.popleft()
            else:
                print('error')
                reverse_flag = -1
                break
        
    if reverse_flag != -1:
        if reverse_flag % 2 == 1:
            deq.reverse()
            
        print('[' + ','.join(deq) + ']') if deq else print('[]')