# source : https://www.acmicpc.net/problem/1874
# data structure, stack

count, is_possible = 0, True
stack, operators = [], []

for i in range(int(input())):
    # input
    number = int(input())
    
    while count < number:
        count += 1
        operators.append("+")
        stack.append(count)
        
    if stack[-1] == number:
        operators.append("-")
        stack.pop()
    else:
        is_possible = False
        
[print(s, end="\n") for s in operators] if is_possible else print("NO")