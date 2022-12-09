# source : https://www.acmicpc.net/problem/15702

import sys
input = sys.stdin.readline

# input
n, m = map(int, input().split())
scores = list(map(int, input().split()))

student_number = 10 ** 6
max_score = 0
for _ in range(m):
    # input
    test_info = input().split()
    
    total = sum([scores[i - 1] for i in range(1, len(test_info)) if test_info[i] == 'O'])
    if total >= max_score:
        curr_std_num = int(test_info[0])
        student_number = min(student_number, curr_std_num) if total == max_score else curr_std_num
        max_score = total    
        
print(student_number, max_score)