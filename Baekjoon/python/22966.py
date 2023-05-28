# source : https://www.acmicpc.net/problem/22966

def main():
    # input
    n = int(input())
    problems = [(input().split()) for _ in range(n)]
    
    problems.sort(key = lambda tu : tu[1])
    
    print(problems[0][0])

if __name__ == '__main__':
    main()