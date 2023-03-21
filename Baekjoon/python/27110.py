# source : https://www.acmicpc.net/problem/27110

def main():
    # input
    n = int(input())
    fried, soy, seasoned = map(int, input().split())
    
    print(min(n, fried) + min(n, soy) + min(n, seasoned))
    
if __name__ == '__main__':
    main()