# source : https://www.acmicpc.net/problem/2828

def main():
    # input
    n, m = map(int, input().split())
    
    start, end = 1, m
    result = 0
    
    # input
    for _ in range(int(input())):
        # input
        screen_num = int(input())
        
        if start <= screen_num <= end:
            continue
        elif start > screen_num:
            result += (start - screen_num)
            end -= (start - screen_num)
            start = screen_num
        else:
            result += (screen_num - end)
            start += (screen_num - end)
            end = screen_num
    
    print(result)
    
if __name__ == '__main__':
    main()