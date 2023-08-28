# source : https://www.acmicpc.net/problem/9469

def main():
    # input
    p = int(input())
    
    for _ in range(p):
        # input
        n, d, a, b, f = map(float, input().split())
        
        print('%d %.6f' % (n, d / (a + b) * f))
        
if __name__ == '__main__':
    main()