# source : https://www.acmicpc.net/problem/15080

def main():
    # input
    sh, sm, ss = map(int, input().split(':'))
    eh, em, es = map(int, input().split(':'))
    
    s = sh * 3600 + sm * 60 + ss
    e = eh * 3600 + em * 60 + es
    
    if s > e:
        print((e - s) + (24 * 3600))
    else:
        print(e - s)

if __name__ == '__main__':
    main()