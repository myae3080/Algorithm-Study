# source : https://www.acmicpc.net/problem/13136

def main():
    # input
    r, c, n = map(int, input().split())
    
    row = (r // n) + (1 if (r % n != 0) else 0)
    col = (c // n) + (1 if (c % n != 0) else 0)
    
    print(row * col)
    
if __name__ == '__main__':
    main()