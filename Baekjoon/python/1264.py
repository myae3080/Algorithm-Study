# string

import sys

# input
input = sys.stdin.readline

vowel_list = ['a', 'e', 'i', 'o', 'u']

while True:
    # input
    input_str = input().rstrip()

    if input_str == '#':
        break
    
    count = 0

    for v in vowel_list:
        count += input_str.count(v)
        count += input_str.count(str.upper(v))

    print(count)