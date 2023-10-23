# source : https://www.acmicpc.net/problem/4084

def main():
    while 1:
        # input
        a, b, c, d = map(int, input().split())
        
        if a == b == c == d == 0:
            break
        
        count = 0
        while not (a == b == c == d):
            count += 1
            a, b, c, d = abs(a - b), abs(b - c), abs(c - d), abs(d - a)

        print(count)

if __name__ == '__main__':
    main()