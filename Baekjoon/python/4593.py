# source : https://www.acmicpc.net/problem/4593

def main():
    while 1:
        # input
        a, b = input(), input()
        
        if a == b == 'E':
            break
        
        p1, p2 = 0, 0
        for i in range(len(a)):
            if (a[i] == 'R' and b[i] == 'S') or (a[i] == 'S' and b[i] == 'P') or (a[i] == 'P' and b[i] == 'R'):
                p1 += 1
            
            if (b[i] == 'R' and a[i] == 'S') or (b[i] == 'S' and a[i] == 'P') or (b[i] == 'P' and a[i] == 'R'):
                p2 += 1
    
        print('P1: %d' % p1)
        print('P2: %d' % p2)

if __name__ == '__main__':
    main()