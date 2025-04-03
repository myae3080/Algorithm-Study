# source : https://www.acmicpc.net/problem/26082

def main():
    # input
    A, B, C = map(int, input().split())
    
    print((B // A) * C * 3)

if __name__ == '__main__':
    main()