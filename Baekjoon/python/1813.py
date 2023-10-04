# source : https://www.acmicpc.net/problem/1813

def main():
    # input
    n = int(input())
    problems = list(map(int, input().split()))
    
    result = -1
    for i in range(n + 1):
        if problems.count(i) == i:
            result = max(result, i)
    
    print(result)
    
if __name__ == '__main__':
    main()