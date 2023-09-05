# source : https://www.acmicpc.net/problem/15780

def main():
    # input
    n, k = map(int, input().split())
    multi_tabs = list(map(int, input().split()))
    
    total_tabs = 0
    for tab in multi_tabs:
        if tab % 2 == 0:
            total_tabs += tab // 2
        else:
            total_tabs += (tab // 2) + 1
            
    print('YES' if total_tabs >= n else 'NO')

if __name__ == '__main__':
    main()