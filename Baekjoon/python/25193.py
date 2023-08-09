# source : https://www.acmicpc.net/problem/25193

def main():
    # input
    n = int(input())
    menu = input()
    
    if n == menu.count('C'):
        print(n)
    else:
        others = n - menu.count('C')
        
        print(n // (others + 1))
        
if __name__ == '__main__':
    main()