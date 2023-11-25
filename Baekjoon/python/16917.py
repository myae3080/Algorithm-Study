# source : https://www.acmicpc.net/problem/16917

def main():
    # input
    a, b, c, x, y = map(int, input().split())

    half = min(x, y)
    if (a + b) // 2 > c:
        result = (half * c * 2) + ((x - half) * min(c * 2, a)) + ((y - half) * min(c * 2, b)) 
    else:
        result = (a * x) + (b * y)

    print(result)

if __name__ == '__main__':
    main()