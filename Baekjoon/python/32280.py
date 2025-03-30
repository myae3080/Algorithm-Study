# source : https://www.acmicpc.net/problem/32280

import sys

input = sys.stdin.readline

def main():
    # input
    N = int(input())
    
    students = []
    teacher = 0
    for _ in range(N + 1):
        # input
        time, type = input().split()
        
        hh, mm = map(int, time.split(':'))
        total_mm = hh * 60 + mm
        if type == 'student':
            students.append(total_mm)
        else:
            teacher = total_mm
    
    # input
    sh, sm = map(int, input().split(':'))
    
    s_total_mm = sh * 60 + sm
    
    result = 0
    if teacher <= s_total_mm:
        for s in students:
            if s >= s_total_mm:
                result += 1
    else:
        for s in students:
            if s >= teacher:
                result += 1
    
    print(result)

if __name__ == '__main__':
    main()