# source : https://www.acmicpc.net/problem/14761

def main():
    # input
    x, y, n = map(int, input().split())
    
    for i in range(1, n + 1):
        if i % x == i % y == 0:
            print('FizzBuzz')
        elif i % x == 0:
            print('Fizz')
        elif i % y == 0:
            print('Buzz')
        else:
            print(i)

if __name__ == '__main__':
    main()