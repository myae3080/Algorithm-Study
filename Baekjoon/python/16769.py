# source : https://www.acmicpc.net/problem/16769

def main():
    # input
    c1, m1 = map(int, input().split())
    c2, m2 = map(int, input().split())
    c3, m3 = map(int, input().split())

    for i in range(1, 101):
        if i % 3 == 1:
            if m1 + m2 > c2:
                m1 = m1 + m2 - c2
                m2 = c2
            else:
                m2 += m1
                m1 = 0
        elif i % 3 == 2:
            if m2 + m3 > c3:
                m2 = m2 + m3 - c3
                m3 = c3
            else:
                m3 += m2
                m2 = 0
        else:
            if m3 + m1 > c1:
                m3 = m3 + m1 - c1
                m1 = c1
            else:
                m1 += m3
                m3 = 0

    print(m1)
    print(m2)
    print(m3)

if __name__ == '__main__':
    main()