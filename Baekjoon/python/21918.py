# source : https://www.acmicpc.net/problem/21918

def main():
    # input
    n, m = map(int, input().split())
    bulbs = list(input().split())
    
    for _ in range(m):
        # input
        a, b, c = map(int, input().split())
        
        if a == 1:
            bulbs[b - 1] = str(c)
        elif a == 2:
            for i in range(b - 1, c):
                if bulbs[i] == '0':
                    bulbs[i] = '1'
                else:
                    bulbs[i] = '0'
        elif a == 3:
            for i in range(b - 1, c):
                bulbs[i] = '0'
        else:
            for i in range(b - 1, c):
                bulbs[i] = '1'
            
    print(' '.join(bulbs))

if __name__ == '__main__':
    main()