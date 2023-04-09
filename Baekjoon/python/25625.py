# source : https://www.acmicpc.net/problem/25625

def main():
    # inbput
    x, y = map(int, input().split())
    
    print(abs(x - y)) if y > x else print(x + y)
    
if __name__ == '__main__':
    main()