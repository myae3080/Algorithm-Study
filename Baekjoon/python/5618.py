# source : https://www.acmicpc.net/problem/5618

def gcd(a, b):
    if a > b: 
        a, b = b, a
        
    if a == 0:
        return b
    
    return gcd(b % a, a)

# input
n = int(input())
nums = list(map(int, input().split()))

gcf = gcd(nums[0], gcd(nums[1], nums[-1]))

# 배열에 담아 한번에 출력하거나, 최대공약수 전체의 범위를 체크하면 시간초과 발생.
for i in range(1, (gcf // 2) + 1):
    if gcf % i == 0:
        print(i)
        
print(gcf)