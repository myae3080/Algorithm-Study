# math

def check_palindrome(str_num):
    check_str_num = str(int(str_num) + int(str_num[::-1]))

    print('YES') if check_str_num == check_str_num[::-1] else print('NO')

    
for i in range(int(input())):
    # input
    check_palindrome(input())