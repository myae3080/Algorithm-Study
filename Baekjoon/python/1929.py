# math, prime number

# 너무 느림
import math

# input
from_num, to_num = map(int, input().split())

for num in range(from_num, to_num + 1):
    is_prime = True

    if num == 1:
        is_prime = False
    else:
        for n in range(2, int(math.sqrt(num)) + 1):
            if num % n == 0 and n != num:
                is_prime = False
                break
    
    if is_prime:
        print(num)