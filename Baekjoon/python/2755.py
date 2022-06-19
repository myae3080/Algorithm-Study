# source : https://www.acmicpc.net/problem/2755

grades = {
    'A+': 4.3, 'A0': 4.0, 'A-':3.7,
    'B+': 3.3, 'B0': 3.0, 'B-':2.7,
    'C+': 2.3, 'C0': 2.0, 'C-':1.7,
    'D+': 1.3, 'D0': 1.0, 'D-':0.7,
    'F': 0.0
}

credits, scores = 0, 0

# TODO : 단순화 필요
# 사사오입 원칙으로 인한 추가 처리
def roundUpTwoPoint(num):
    round_value = round(num, 2)
    
    if int('{:.3f}'.format(num)[-1]) == 5:
        return round_value + 10 ** -2
    else:
        return round_value

for _ in range(int(input())):
    # input
    inputs = input().split()
    
    credit = int(inputs[1])
    
    credits += credit
    scores += (credit * grades[inputs[2]])

print('{:.2f}'.format(roundUpTwoPoint(round(scores / credits, 3))))