# source : https://www.acmicpc.net/problem/2145
# math

while True:
    # input
    num = int(input())
    
    if num == 0:
        break
    
    nums = list(map(int, str(num)))
    
    while len(nums) > 1:
        num = sum(nums)
        nums = list(map(int, str(num)))
        
    print(num)