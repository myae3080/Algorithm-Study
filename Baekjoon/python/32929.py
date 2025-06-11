# source : https://www.acmicpc.net/problem/32929

def main():
    # input
    x = int(input())
    
    mod = x % 3
    if mod == 0:
        print('S')
    elif mod == 1:
        print('U')
    else:
        print('O')

if __name__ == '__main__':
    main()