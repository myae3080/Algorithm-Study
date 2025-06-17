# source : https://www.acmicpc.net/problem/2852

import sys 

input = sys.stdin.readline

def main():
    # input
    N = int(input())
    
    team1_time, team2_time = 0, 0
    team1_prev, team2_prev = 0, 0
    team1_score, team2_score = 0, 0
    for _ in range(N):
        # input
        team, time = input().split()
    
        mm, ss = map(int, time.split(':'))
        total_sec = mm * 60 + ss
        
        if team1_score > team2_score:
            team1_time += (total_sec - team1_prev)
        elif team2_score > team1_score:
            team2_time += (total_sec - team2_prev)
        
        if team == '1':
            team1_score += 1
        elif team == '2':
            team2_score += 1
        
        if team1_score > team2_score:
            team1_prev = total_sec
        elif team2_score > team1_score:
            team2_prev = total_sec
    
    if team1_score > team2_score:
            team1_time += (48 * 60 - team1_prev)
    elif team2_score > team1_score:
        team2_time += (48 * 60 - team2_prev)
    
    print('%s:%s' % (str(team1_time // 60).zfill(2), str(team1_time % 60).zfill(2)))
    print('%s:%s' % (str(team2_time // 60).zfill(2), str(team2_time % 60).zfill(2)))

if __name__ == '__main__':
    main()