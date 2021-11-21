# source : https://www.acmicpc.net/problem/2028
# math

for _ in range(int(input())):
    # input
    num = input()
    square = str(int(num) ** 2)
    
    if square[len(square) - len(num):] == num:
        print("YES")
    else:
        print("NO")