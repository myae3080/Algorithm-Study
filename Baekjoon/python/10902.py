# source : https://www.acmicpc.net/problem/10902

def main():
    f, tf, sf = 0, 0, 0
    
    # input
    for i in range(1, int(input()) + 1):
        # input
        t, s = map(int, input().split())
        
        if s > sf:
            f = i
            tf = t
            sf = s
    
    if sf == 0:
        print(0)
    else:
        print(tf + (f - 1) * 20)

if __name__ == '__main__':
    main()