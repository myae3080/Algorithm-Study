# dp

# input
input_num = int(input())

# 습관적으로 무턱대고 풀다가 오래 걸린 케이스. 규칙성을 찾는 것이 중요.
one_list = [0] * (input_num + 1)

for i in range(2, input_num + 1):
    one_list[i] = one_list[i - 1] + 1

    if i % 3 == 0:
        one_list[i] = min(one_list[i // 3] + 1, one_list[i])

    if i % 2 == 0:
        one_list[i] = min(one_list[i // 2] + 1, one_list[i])
    
print(one_list[input_num])