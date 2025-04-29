# source : https://www.acmicpc.net/problem/32306

def main():
    # input
    team1, team2 = list(map(int, input().split())), list(map(int, input().split()))

    score1 = sum([team1[i] * (i + 1) for i in range(len(team1))])
    score2 = sum([team2[i] * (i + 1) for i in range(len(team2))])

    if score1 == score2:
        print(0)
    elif score1 > score2:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    main()