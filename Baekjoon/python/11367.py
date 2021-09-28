# source : https://www.acmicpc.net/problem/11367
# string

def score_check(score):
    if score >= 97:
        return 'A+'
    elif score >= 90:
        return 'A'
    elif score >= 87:
        return 'B+'
    elif score >= 80:
        return 'B'
    elif score >= 77:
        return 'C+'
    elif score >= 70:
        return 'C'
    elif score >= 67:
        return 'D+'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

for _ in range(int(input())):
    # input
    name, score = input().split()

    print(name, score_check(int(score)))