# source : https://www.acmicpc.net/problem/8595

import re

# input
n, word = int(input()), input()

result = 0
for s in re.split(r'[a-zA-Z]', word):
    if s.isdigit():
        result += int(s)
        
print(result)