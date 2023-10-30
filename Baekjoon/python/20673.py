# source : https://www.acmicpc.net/problem/20673

def main():
    # input
    p, q = int(input()), int(input())
    
    if p <= 50 and q <= 10:
        print('White')
    elif q > 30:
        print('Red')
    else:
        print('Yellow')

if __name__ == '__main__':
    main()