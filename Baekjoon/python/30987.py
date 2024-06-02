# source : https://www.acmicpc.net/problem/30987

def main():
    # input
    x1, x2 = map(int, input().split())
    a, b, c, d, e = map(int, input().split())
    
    def integral(x: int) -> int:
        return ((a * (x ** 3)) // 3 + (((b - d) * (x ** 2)) // 2) + ((c - e) * x))

    print(integral(x2) - integral(x1))

if __name__ == '__main__':
    main()