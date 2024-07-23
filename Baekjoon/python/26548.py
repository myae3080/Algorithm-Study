# source : https://www.acmicpc.net/problem/26548

def main():
    # input
    n = int(input())
    
    for _ in range(n):
        # input
        a, b, c = map(float, input().split())
        
        root = (b ** 2 - 4 * a * c) ** 0.5
        
        print('%.3f, %.3f' % (round((-b + root) / (2 * a), 3), round((-b - root) / (2 * a), 3)))

if __name__ == '__main__':
    main()