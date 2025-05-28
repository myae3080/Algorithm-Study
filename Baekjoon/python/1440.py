# source : https://www.acmicpc.net/problem/1440

def main():
    # input
    num1, num2, num3 = map(int, input().split(':'))
    
    if num1 == num2 == num3 == 0:
        print(0)
        
        return
    
    result = 0
    if 1 <= num1 <= 12 and 0 <= num2 <= 59 and 0 <= num3 <= 59:
        result += 2
    if 1 <= num2 <= 12 and 0 <= num1 <= 59 and 0 <= num3 <= 59:
        result += 2
    if 1 <= num3 <= 12 and 0 <= num1 <= 59 and 0 <= num2 <= 59:
        result += 2
    
    print(result)

if __name__ == '__main__':
    main()