# source : https://www.acmicpc.net/problem/32184

def main():
    # input
    A, B = map(int, input().split())
    
    common = (B - A) // 2
    if A % 2 == 0 and B % 2 != 0:
        print(common + 2)
    else:
        print(common + 1)

if __name__ == '__main__':
    main()