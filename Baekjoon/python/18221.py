# source : https://www.acmicpc.net/problem/18221

import sys

input = sys.stdin.readline

def main():
    # input
    N = int(input())
    
    professor_seat, sk_seat = (0, 0), (0, 0)
    students_seat = []
    cnt = 0
    for i in range(N):
        # input
        seat = list(input().rstrip().split())
        
        if seat.count('5'):
            professor_seat = (seat.index('5'), i)
        if seat.count('2'):
            sk_seat = (seat.index('2'), i)
        if seat.count('1'):
            for j in range(N):
                if seat[j] == '1':
                    students_seat.append((j, i))
    
    x1, y1 = min(professor_seat[0], sk_seat[0]), min(professor_seat[1], sk_seat[1])
    x2, y2 = max(professor_seat[0], sk_seat[0]), max(professor_seat[1], sk_seat[1])
    for seat in students_seat:
        if x1 <= seat[0] <= x2 and y1 <= seat[1] <= y2:
            cnt += 1
    
    if cnt >= 3 and (x1 - x2) ** 2 + (y1 - y2) ** 2 >= 25:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()