# source : https://www.acmicpc.net/problem/13234

def main():
    # input
    a, operator, b = input().split()
    
    if operator == 'AND':
        if a == 'true' and b == 'true':
            print('true')
        else:
            print('false')
    else:
        if a == 'false' and b == 'false':
            print('false')
        else:
            print('true')

if __name__ == '__main__':
    main()