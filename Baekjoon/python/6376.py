# source : https://www.acmicpc.net/problem/6376

def main():
    print('n', 'e')
    print('- -----------')
    
    n, answer = 0, 0
    while n < 10:
        answer += (1 / factorial(n))
        
        if answer <= 2:
            print(n, int(answer))
        elif answer <= 2.5:
            print(n, '{:.1f}'.format(answer))
        else:
            print(n, '{:.9f}'.format(answer))
        
        n += 1

def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
        
    return result

if __name__ == '__main__':
    main()