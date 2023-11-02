# source : https://www.acmicpc.net/problem/25642

def main():
    # input
    a, b = map(int, input().split())
    
    isYT = True
    while a < 5 and b < 5:
        if isYT:
            b += a
            isYT = False
        else:
            a += b
            isYT = True
    
    print('yj' if a > b else 'yt')

if __name__ == '__main__':
    main()