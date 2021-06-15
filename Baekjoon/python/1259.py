# palindrome

while True:
    # input
    input_str = input()

    if input_str == '0':
        break

    half = len(input_str) // 2

    if len(input_str) == 1:
        print('yes')
    else: 
        for i in range(half):
            if input_str[i] != input_str[len(input_str) - i - 1]:
                print('no')
                break
        
            if i == half - 1:
                print('yes')