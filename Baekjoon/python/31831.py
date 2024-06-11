# source : https://www.acmicpc.net/problem/31831

def main():
    # input
    n, m = map(int, input().split())
    stress = list(map(int, input().split()))
    
    status, result = 0, 0
    for s in stress:
        status = max(0, status + s)
        
        if status >= m:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()