# source : https://www.acmicpc.net/problem/30999

def main():
    # input
    n, m = map(int, input().split())
    
    result = 0
    for _ in range(n):
        # input
        problem = input()
        
        result += 1 if problem.count('O') > m // 2 else 0
    
    print(result)

if __name__ == '__main__':
    main()