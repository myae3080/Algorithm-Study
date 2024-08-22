# source : https://www.acmicpc.net/problem/2061

def main():
    # input
    K, L = map(int, input().split())
    
    is_bad = False
    for n in range(2, L):
        if K % n == 0:
            print('BAD', n)
            is_bad = True
            break
    
    if not is_bad:
        print('GOOD')

if __name__ == '__main__':
    main()