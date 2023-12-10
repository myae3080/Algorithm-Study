# source : https://www.acmicpc.net/problem/9471
# Piasno period

def main():
    # input
    for _ in range(int(input())):
        # input
        n, m = map(int, input().split())
        
        result = 1
        p1, p2 = 1, 2
        while 1:
            if p1 % m == 1 and p2 % m == 1:
                break
            
            result += 1
            p1, p2 = p2 % m, (p1 + p2) % m
        
        print('%d %d' % (n, result))

if __name__ == '__main__':
    main()