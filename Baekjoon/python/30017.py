# source : https://www.acmicpc.net/problem/30017

def main():
    # input
    patty, cheese = map(int, input().split())
    
    base = min(patty - 2, cheese - 1)
    
    print(3 + 2 * base)

if __name__ == '__main__':
    main()