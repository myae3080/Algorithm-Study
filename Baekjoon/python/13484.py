# source : https://www.acmicpc.net/problem/13484

def main():
    # input
    x = int(input())
    n = int(input())
    
    total = x * (n + 1)
    for _ in range(n):
        # input
        mb = int(input())
        
        total -= mb
    
    print(total)

if __name__ == '__main__':
    main()