# source : https://www.acmicpc.net/problem/15784

def main():
    # input
    n, a, b = map(int, input().split())
    chairs = [list(map(int, input().split())) for _ in range(n)]
    
    attractiveness = chairs[a - 1]
    for i in range(n):
        attractiveness.append(chairs[i][b - 1])
    
    print('ANGRY' if chairs[a - 1][b - 1] < max(attractiveness) else 'HAPPY')
    
if __name__ == '__main__':
    main()