# source : https://www.acmicpc.net/problem/14790

def main():
    # input
    for i in range(1, int(input()) + 1):
        # input
        N = int(input())
        
        for n in range(N, 0, -1):
            if str(n) == ''.join(sorted(list(str(n)))):
                print('Case #%d: %d' % (i, n))
                
                break

if __name__ == '__main__':
    main()