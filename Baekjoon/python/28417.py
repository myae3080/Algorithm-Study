# source : https://www.acmicpc.net/problem/28417

def main():
    # input
    n = int(input())
    
    result = 0
    for _ in range(n):
        # input
        scores = list(map(int, input().split()))
        
        result = max(result, max(scores[:2]) + sum(sorted(scores[2:], reverse=True)[:2]))
    
    print(result)

if __name__ == '__main__':
    main()