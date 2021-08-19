# source : https://www.acmicpc.net/problem/3036
# math, number theory, Euclidean algorithm

def gcd(a, b):
    if a > b: 
        a, b = b, a

    if a == 0:
        return b
    else:
        return gcd(b % a, a)

# input
n = int(input())
circle_list = list(map(int, input().split()))

first_circle = circle_list[0]

for r in circle_list[1:]:
    gcd_num = gcd(first_circle, r)
    print(str(first_circle // gcd_num) + '/' + str(r // gcd_num))