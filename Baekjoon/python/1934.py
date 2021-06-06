# math, least common multiple

# input
count = int(input())

# Euclidean algorithm
def gcd(large_num, small_num):
    if small_num == 0:
        return large_num

    if large_num % small_num == 0:
        return small_num
    else:
        return gcd(small_num, large_num % small_num)

for i in range(count):
    num1, num2 = map(int, input().split())

    gcd_num = gcd(num2, num1)

    print((num1 * num2) // gcd_num)