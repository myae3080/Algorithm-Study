# source : https://www.acmicpc.net/problem/3058
# math

def printEvenSumAndMin(nums: list):
    # exception handling
    if not nums:
        return
    
    even_nums = []
    
    for n in nums:
        if n % 2 == 0:
            even_nums.append(n)
    
    print(sum(even_nums), min(even_nums))
    
# input
for _ in range(int(input())):
    printEvenSumAndMin(list(map(int, input().split())))