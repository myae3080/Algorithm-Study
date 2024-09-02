# source : https://www.acmicpc.net/problem/5101

def main():
    while 1:
        # input
        a, d, c = map(int, input().split())
        
        if a == d == c == 0:
            break
        
        if (c - a) % d == 0 and (c - a) // d >= 0:
            print(abs((c - a) // d) + 1)
        else:
            print('X')

if __name__ == '__main__':
    main()