# source : https://www.acmicpc.net/problem/6322

def main():
    i = 1
    while 1:
        # input
        a, b, c = map(int, input().split())
        
        if a == b == c == 0:
            break
        
        print('Triangle #' + str(i))
        if c == -1:
            print('c =', '{:.3f}'.format((a ** 2 + b ** 2) ** 0.5))
        else:
            if max(a, b) >= c:
                print('Impossible.')
            else:
                if a == -1:
                    print('a =', '{:.3f}'.format((c ** 2 - b ** 2) ** 0.5))
                else:
                    print('b =', '{:.3f}'.format((c ** 2 - a ** 2) ** 0.5))

        i += 1
        print()

if __name__ == '__main__':
    main()