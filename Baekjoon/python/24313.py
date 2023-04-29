# source : https://www.acmicpc.net/problem/24313

def main():
    # input
    a1, a0 = map(int, input().split())
    c = int(input())
    n0 = int(input())
    
    if a1 * n0 + a0 > c * n0 or c < a1:
        print(0)
    else:
        print(1)
    
if __name__ == '__main__':
    main()