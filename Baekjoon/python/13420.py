# source : https://www.acmicpc.net/problem/13420
# string

for _ in range(int(input())):
    # input
    input_list = list(input().split())
    a, b, operator, result = int(input_list[0]), int(input_list[2]), input_list[1], int(input_list[-1])
    correct = 0

    if operator == "+":
        correct = a + b
    elif operator == "-":
        correct = a - b
    elif operator == "*":
        correct = a * b
    else:
        correct = a / b
    
    print("correct") if correct == result else print("wrong answer")