# source : https://www.acmicpc.net/problem/6856

def main():
    # input
    m, n = int(input()), int(input())
    
    result = 0
    for i in range(1, m + 1):
        for j in range(n, 0, -1):
            if i + j == 10:
                result += 1
                break
    
    if result == 1:
        print('There is %d way to get the sum 10.' % result)
    else:
        print('There are %d ways to get the sum 10.' % result)

if __name__ == '__main__':
    main()