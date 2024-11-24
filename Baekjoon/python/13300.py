# source : https://www.acmicpc.net/problem/13300

import sys
input = sys.stdin.readline

def main():
    # input
    N, K = map(int, input().split())
    
    stu_num_by_grade = {}
    for _ in range(N):
        # input
        S, grade = map(int, input().split())
        
        if grade not in stu_num_by_grade:
            stu_num_by_grade[grade] = {S: 1}
        else:
            if S not in stu_num_by_grade[grade]:
                stu_num_by_grade[grade][S] = 1
            else:
                stu_num_by_grade[grade][S] += 1
    
    result = 0
    for grade in stu_num_by_grade:
        for s in stu_num_by_grade[grade].keys():
            stu_num = stu_num_by_grade[grade][s]
            result += stu_num // K if stu_num % K == 0 else (stu_num // K) + 1
    
    print(result)

if __name__ == '__main__':
    main()