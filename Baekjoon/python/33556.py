# source : https://www.acmicpc.net/problem/33556

def main():
    # input
    A, B = input(), input()
    
    if A == 'null':
        print('NullPointerException')
        print('NullPointerException')
    elif B == 'null':
        print('false')
        print('false')
    else:
        print('true' if A == B else 'false')
        print('true' if A.lower() == B.lower() else 'false')

if __name__ == '__main__':
    main()