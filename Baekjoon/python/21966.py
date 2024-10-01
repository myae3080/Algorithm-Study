# source : https://www.acmicpc.net/problem/21966

def main():
    # input
    N = int(input())
    S = input()
    
    if N <= 25:
        print(S)
    else:
        mid = S[11:-11]
        if '.' in mid and '.' in mid[:-1]:
                print(S[:9] + '......' + S[-10:])
        else:
            print(S[:11] + '...' + S[-11:])

if __name__ == '__main__':
    main()