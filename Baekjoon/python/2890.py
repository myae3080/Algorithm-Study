# source : https://www.acmicpc.net/problem/2890

def main():
    # input
    R, C = map(int, input().split())
    
    teams_by_distance = {}
    for _ in range(R):
        # input
        lane = input()
        
        team = lane.replace('.', '').replace('S', '').replace('F', '')
        if not team:
            continue
        
        if C - lane.find(team) not in teams_by_distance:
            teams_by_distance[C - lane.find(team)] = [int(team[0])]
        else:
            teams_by_distance[C - lane.find(team)].append(int(team[0]))
        
    result = [0] * 10
    rank = 1
    for d in sorted(teams_by_distance.keys()):
        for team in teams_by_distance[d]:
            result[team] = rank
        
        rank += 1
    
    for rank in result[1:]:
        print(rank)

if __name__ == '__main__':
    main()