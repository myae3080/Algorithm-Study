# source : https://www.acmicpc.net/problem/23808

def main():
    # input
    n = int(input())
    
    for _ in range(n * 2):
        print('@' * n + ' ' * (n * 3) + '@' * n)
    
    for _ in range(n):
        print('@' * n * 5)
        
    for _ in range(n):
        print('@' * n + ' ' * (n * 3) + '@' * n)
        
    for _ in range(n):
        print('@' * n * 5)
    
if __name__ == '__main__':
    main()