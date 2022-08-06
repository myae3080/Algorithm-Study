# source : https://www.acmicpc.net/problem/10448

triangular_numbers = [(i * (i + 1)) // 2 for i in range(1, 45)]
eureka = [0] * 1001

for num1 in triangular_numbers:
    for num2 in triangular_numbers:
        for num3 in triangular_numbers:
            if num1 + num2 + num3 <= 1000:
                eureka[num1 + num2 + num3] = 1

for _ in range(int(input())):
    # input
    print(eureka[int(input())])