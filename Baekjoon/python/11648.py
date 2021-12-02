# source : https://www.acmicpc.net/problem/11648
# math

# input
input_str = input()

count = 0

while True:
    nums = list(map(int, input_str))
    temp = 1
    
    if len(nums) == 1:
        break
    else:
        count += 1
        
        for n in nums:
            temp *= n
            
        input_str = str(temp)

print(count)