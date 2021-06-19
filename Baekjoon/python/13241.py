# lcm

def gcd(large_num, small_num):
    # 함수를 사용 하는 사용자가 실수를 했을 때를 대비한 코딩
    if large_num < small_num:
        large_num, small_num = small_num, large_num

    if small_num == 0:
        return large_num
    
    if large_num % small_num == 0:
        return small_num
    else:
        return gcd(small_num, large_num % small_num)

# input
a, b = map(int, input().split())

print(int(a * b / gcd(a, b)))