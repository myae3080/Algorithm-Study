# source : https://www.acmicpc.net/problem/18127

def main():
    # input
    A, B = map(int, input().split())

    a, d = 1, A - 2
    l = a + (B * d)
    
    print(((B + 1) * (a + l)) // 2)

if __name__ == '__main__':
    main()