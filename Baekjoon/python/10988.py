# string, palindrome

# input
input_str = input()

string_length = len(input_str)
is_palindrome = True

for i in range(string_length):
    if input_str[i] != input_str[string_length - i - 1]:
        is_palindrome = False
        break

print(1) if is_palindrome else print(0)
