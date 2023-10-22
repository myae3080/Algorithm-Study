# source : https://www.acmicpc.net/problem/29752

def main():
    # input
    n = int(input())
    solved = list(map(int, input().split()))
    
    result = []
    streak = 0
    for i in range(n):
        if solved[i] == 0:
            result.append(streak)
            streak = 0
        else:
            streak += 1
            
        if i == (n - 1):
            result.append(streak)

    print(max(result))

if __name__ == '__main__':
    main()