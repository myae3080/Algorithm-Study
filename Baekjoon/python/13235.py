# source : https://www.acmicpc.net/problem/13235
# string

# input
input_str = input()

length = len(input_str)
half = length // 2
is_palindrome = 'true'

for i in range(half):
    if input_str[i] != input_str[length - 1 - i]:
        is_palindrome = 'false'
        break

print(is_palindrome)