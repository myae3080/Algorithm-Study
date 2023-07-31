# source : https://www.acmicpc.net/problem/25024

def main():
    # input
    for _ in range(int(input())):
        # input
        x, y = map(int, input().split())
        
        if 0 <= x <= 23 and 0 <= y <= 59:
            print('Yes', end=' ')
        else:
            print('No', end=' ')
            
        if x in [1, 3, 5, 7, 8, 10, 12] and 1 <= y <= 31:
            print('Yes')
        elif x in [4, 6, 9, 11] and 1 <= y <= 30:
            print('Yes')
        elif x == 2 and 1 <= y <= 29:
            print('Yes')
        else:
            print('No')
            
if __name__ == '__main__':
    main()