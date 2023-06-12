# source : https://www.acmicpc.net/problem/15025

def main():
    # input
    l, r = map(int, input().split())
    
    if l == r == 0:
        print('Not a moose')
    else:
        print('Even', l + r) if l == r else print('Odd', max(l, r) * 2)
        
if __name__ == '__main__':
    main()