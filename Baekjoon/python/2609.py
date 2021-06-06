# math, greatest common factor, least common multiple

# input
num1, num2 = map(int, input().split())

def gcd(large_num, small_num):
    if small_num == 0:
        return large_num
    
    if large_num % small_num == 0:
        return small_num
    else:
        return gcd(small_num, large_num % small_num)

if num1 > num2:
    num1, num2 = num2, num1

gcd_num = gcd(num2, num1)
lcm_num = (num1 * num2 // gcd_num)

print(gcd_num)
print(lcm_num)