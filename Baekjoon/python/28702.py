# source : https://www.acmicpc.net/problem/28702

def main():
    # input
    words = [input() for _ in range(3)]
    
    num = 0
    if words[-1].isdigit():
        num = int(words[-1]) + 1
    else:
        if words[0].isdigit():
            num = int(words[0]) + 3
        else:
            num = int(words[1]) + 2
    
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 5 == 0:
        print('Buzz')
    elif num % 3 == 0:
        print('Fizz')
    else:
        print(num)

if __name__ == '__main__':
    main()