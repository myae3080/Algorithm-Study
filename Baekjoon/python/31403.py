# source : https://www.acmicpc.net/problem/31403

def main():
    # input
    a, b, c = input(), input(), int(input())
    
    print(int(a) + int(b) - c)
    print(int(a + b) - c)

if __name__ == '__main__':
    main()