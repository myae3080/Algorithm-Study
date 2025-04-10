# source : https://www.acmicpc.net/problem/27590

def main():
    # input
    ds, ys = map(int, input().split())
    dm, ym = map(int, input().split())
    
    year = 1
    while 1:
        ds += 1
        dm += 1
        if ds % ys == 0 and dm % ym == 0:
            print(year)
            
            break
        
        year += 1

if __name__ == '__main__':
    main()