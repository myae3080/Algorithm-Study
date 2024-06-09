# source : https://www.acmicpc.net/problem/26592

def main():
    # input
    for _ in range(int(input())):
        # input
        area, base = map(float, input().split())
        
        print('The height of the triangle is %.2f units' % ((area / base) * 2))

if __name__ == '__main__':
    main()