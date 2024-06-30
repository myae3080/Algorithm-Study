# source : https://www.acmicpc.net/problem/21185

def main():
    # input
    n = int(input())
    
    if n % 4 == 0:
        print('Even')
    elif n % 2 == 0:
        print('Odd')
    else:
        print('Either')

if __name__ == '__main__':
    main()