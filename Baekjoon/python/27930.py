# source : https://www.acmicpc.net/problem/27930

def main():
    y, k = 'YONSEI', 'KOREA'
    
    # input
    S = input()
    
    for c in S:
        if c == y[0]:
            y = y[1:]
            
        if c == k[0]:
            k = k[1:]
        
        if len(y) == 0:
            print('YONSEI')
            break
        
        if len(k) == 0:
            print('KOREA')
            break

if __name__ == '__main__':
    main()