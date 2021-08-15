# source : https://www.acmicpc.net/problem/14490
# math, string, number theory, parsing, Euclidean algorithm

def gcd(a, b):
    if a > b: 
        a, b = b, a

    if a == 0:
        return b
    else:
        return gcd(b % a, a)

# input
n, m = map(int, input().split(':'))

gcd_num = gcd(n, m)

print(str(n // gcd_num) + ':' + str(m // gcd_num))