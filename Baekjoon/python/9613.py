# source : https://www.acmicpc.net/problem/9613
# math, number theory, Euclidean Algorithm

import sys

# input
input = sys.stdin.readline

def gcd(a, b):
    if a > b: 
        a, b = b, a

    if a == 0:
        return b
    else:
        return gcd(b % a, a)

for _ in range(int(input())):
    # input
    input_list = list(map(int, input().split()))
    n = input_list[0]
    num_list = input_list[1:]

    total_sum = 0

    for i in range(n):
        temp = num_list[i]

        if i != n - 1:
            for j in range(i + 1, n):
                total_sum += gcd(temp, num_list[j])

    print(total_sum)