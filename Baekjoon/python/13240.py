# source : https://www.acmicpc.net/problem/13240

def main():
    # input
    N, M = map(int, input().split())
    
    result = []
    for i in range(N):
        row = '.' if i % 2 else '*'
        
        for j in range(1, M):
            if row[0] == '*':
                row += '.' if j % 2 else '*'
            else:
                row += '*' if j % 2 else '.'
        
        result.append(row)
    
    for r in result:
        print(r)

if __name__ == '__main__':
    main()