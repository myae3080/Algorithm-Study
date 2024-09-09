# source : https://www.acmicpc.net/problem/26575

def main():
    # input
    for _ in range(int(input())):
        # input
        d, f, p = map(float, input().split())
        
        print('${:.2f}'.format(d * f * p))

if __name__ == '__main__':
    main()