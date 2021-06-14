# math, Euclidean Algorithm, GCD, LCM

import math

# input
gcd, lcm = map(int, input().split())

def fn_gcd(a, b):
    while b > 0:
        temp = b
        b = a % b
        a = temp

    return a

if gcd == lcm:
    print(gcd, lcm)
else:
    multiplied_num = lcm * gcd

    sq = int(math.sqrt(multiplied_num))

    for num in reversed(range(sq + 1)):
        if multiplied_num % num == 0:
            if fn_gcd(num , multiplied_num // num) == gcd:
                print(num, multiplied_num // num)
                break