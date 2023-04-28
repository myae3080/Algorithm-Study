# source : https://www.acmicpc.net/problem/10811

def main():
    # input
    n, m = map(int, input().split())
    baskets = [i for i in range(1, n + 1)]
    
    for _ in range(m):
        # input
        i, j = map(int, input().split())
        
        baskets = baskets[:i - 1] + baskets[i - 1:j][::-1] + baskets[j:]
    
    [print(num, end=' ') for num in baskets]
    
if __name__ == '__main__':
    main()