# source : https://www.acmicpc.net/problem/16485

def main():
    # input
    c, b = map(int, input().split())
    
    print(c // b) if c % b == 0 else print('%.10f'%(c / b))

if __name__ == '__main__':
    main()