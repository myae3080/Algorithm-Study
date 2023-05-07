# source : https://www.acmicpc.net/problem/2547

def main():
    # input
    t = int(input())
    
    for _ in range(t):
        # input
        blank = input()
        n = int(input())
        candies = sum([int(input()) for __ in range(n)])
        
        print('YES') if candies % n == 0 else print('NO')
    
if __name__ == '__main__':
    main()