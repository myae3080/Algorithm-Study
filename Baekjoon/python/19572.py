# source : https://www.acmicpc.net/problem/19572

def main():
    # input
    d1, d2, d3 = map(int, input().split())
    
    a = (d1 + d2 - d3) / 2
    b = d1 - a
    c = d2 - a
    
    if a > 0 and b > 0 and c > 0:
        print(1)
        print('{:.1f} {:.1f} {:.1f}'.format(a, b, c))
    else:
        print(-1)
    
if __name__ == '__main__':
    main()