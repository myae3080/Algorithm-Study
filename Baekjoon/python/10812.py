# source : https://www.acmicpc.net/problem/10812

def main():
    # input
    n, m = map(int, input().split())
    
    baskets = [str(i) for i in range(1, n + 1)]
    
    for _ in range(m):
        # input
        i, j, k = map(int, input().split())
    
        baskets = baskets[:i - 1] + baskets[k - 1:j] + baskets[i - 1:k - 1] + baskets[j:]
    
    print(' '.join(baskets))

if __name__ == '__main__':
    main()