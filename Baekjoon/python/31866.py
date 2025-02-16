# source : https://www.acmicpc.net/problem/31866

def main():
    # input
    a, b = map(int, input().split())
    
    rsp = [0, 2, 5]
    if a == b:
        print('=')
    elif a in rsp and b not in rsp:
        print('>')
    elif a not in rsp and b in rsp:
        print('<')
    else:
        if a == 0 and b == 2:
            print('>')
        elif a == 2 and b == 5:
            print('>')
        elif a == 5 and b == 0:
            print('>')
        elif a == 0 and b == 5:
            print('<')
        elif a == 2 and b == 0:
            print('<')
        elif a == 5 and b == 2:
            print('<')
        else:
            print('=')

if __name__ == '__main__':
    main()