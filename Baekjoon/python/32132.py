# source : https://www.acmicpc.net/problem/32132

def main():
    # input
    N = int(input())
    s = input()

    while 1:
        if 'PS4' in s or 'PS5' in s:
            s = s.replace('PS4', 'PS').replace('PS5', 'PS')
        else:
            break
    
    print(s)
    
if __name__ == '__main__':
    main()