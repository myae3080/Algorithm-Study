# source : https://www.acmicpc.net/problem/14175

def main():
    # input
    m, n, k = map(int, input().split())
    paper = [list(input()) for _ in range(m)]
    
    for line in paper:
        result = ''
        for i in range(n):
            result += line[i] * k
        
        for _ in range(k):
            print(result)

if __name__ == '__main__':
    main()