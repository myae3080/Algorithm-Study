# source : https://www.acmicpc.net/problem/31533

def main():
    # input
    a = int(input())
    m, n = map(int, input().split())

    case1 = min(max(m / a, n), 2 * min(m / a, n))
    case2 = min(max(m, n / a), 2 * min(m, n / a))

    print(f"{min(case1, case2):.7f}")

if __name__ == '__main__':
    main()