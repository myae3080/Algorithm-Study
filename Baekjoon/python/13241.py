# lcm

def gcd(large_num, small_num):
    if small_num == 0:
        return large_num
    
    if large_num % small_num == 0:
        return small_num
    else:
        return gcd(small_num, large_num % small_num)

# input
a, b = map(int, input().split())

if b > a:
    a, b = b, a

print(int(a * b / gcd(a, b)))