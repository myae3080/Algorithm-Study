# source : https://www.acmicpc.net/problem/14913

def main():
    # input
    a, d, k = map(int, input().split())
    
    n = (k - a) / d + 1
    print(int(n)) if float(n).is_integer() and n > 0 else print('X')

if __name__ == '__main__':
    main()