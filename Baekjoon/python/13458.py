# math

import math

count = 0

# input
n = int(input())
a_list = list(map(int, input().split()))
b, c = map(int, input().split())

for i in a_list:
    count += 1
    i -= b
    
    if i > 0:
        count += int(math.ceil(i / c))

print(count)