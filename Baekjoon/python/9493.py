# source : https://www.acmicpc.net/problem/9493

def main():
    while 1:
        # input
        m, a, b = map(int, input().split())
        
        if m == a == b == 0:
            break
        
        time = round((m / a - m / b) * 3600)
        ss = time % 60
        time //= 60
        mm = time % 60
        time //= 60
        
        print('%d:%02d:%02d' % (time, mm, ss))

if __name__ == '__main__':
    main()