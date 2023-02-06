# source : https://www.acmicpc.net/problem/16199

def main():
    # input
    y, m, d = map(int, input().split())
    base_y, base_m, base_d = map(int, input().split())

    year_diff = base_y - y

    # 만 나이
    if (m < base_m) or (m == base_m and d <= base_d):
        print(year_diff)
    else:
        print(year_diff - 1)

    # 세는 나이
    print(year_diff + 1)

    # 연 나이
    print(year_diff)

if __name__ == "__main__":
    main()