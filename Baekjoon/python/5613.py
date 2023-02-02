# source : https://www.acmicpc.net/problem/5613

def main():
    # input
    result = int(input())
    
    while 1:
        # input
        operator = input()
        
        if operator == '=':
            break
        
        # input
        number = int(input())
        
        if operator == '+':
            result += number
        elif operator == '-':
            result -= number
        elif operator == '*':
            result *= number
        else:
            result //= number
    
    print(result)

if __name__ == '__main__':
    main()