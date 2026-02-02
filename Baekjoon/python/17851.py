# source : https://www.acmicpc.net/problem/17851

def main():
    # input
    team1, team2 = sorted(list(map(int, input().split()))), sorted(list(map(int, input().split())))

    result = 0
    for i in range(len(team1)):
        if team1[i] > team2[i]:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()