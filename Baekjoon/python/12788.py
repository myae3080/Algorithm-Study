# source : https://www.acmicpc.net/problem/12788

def main():
    # input
    n = int(input())
    m, k = map(int, input().split())
    pen = list(map(int, input().split()))
    
    pens = m * k
    result = 0
    for p in sorted(pen, reverse=True):
        if pens > 0:
            pens -= p
            result += 1
        else:
            break
    
    print('STRESS' if pens > 0 else result)

if __name__ == '__main__':
    main()