# source : https://www.acmicpc.net/problem/10698
# math

for i in range(int(input())):
    # input
    input_list = list(input().split())
    
    a, b, operator, result = int(input_list[0]), int(input_list[2]), input_list[1], int(input_list[-1])
    answer = 0

    if operator == "+":
        answer = a + b
    else:
        answer = a - b

    print("Case " + str(i + 1) + ": YES") if result == answer else print("Case " + str(i + 1) + ": NO")