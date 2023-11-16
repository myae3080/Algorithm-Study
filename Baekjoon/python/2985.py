# source : https://www.acmicpc.net/problem/2985

def main():
    # input
    a, b, c = map(int, input().split())
    
    if a + b == c:
        print('{0}+{1}={2}'.format(a, b, c))
    elif a - b == c:
        print('{0}-{1}={2}'.format(a, b, c))
    elif a * b == c:
        print('{0}*{1}={2}'.format(a, b, c))
    elif a / b == c:
        print('{0}/{1}={2}'.format(a, b, c))
    elif a == b + c:
        print('{0}={1}+{2}'.format(a, b, c))
    elif a == b - c:
        print('{0}={1}-{2}'.format(a, b, c))
    elif a == b * c:
        print('{0}={1}*{2}'.format(a, b, c))
    elif a == b / c:
        print('{0}={1}/{2}'.format(a, b, c))

if __name__ == '__main__':
    main()