# source : https://www.acmicpc.net/problem/31789

import sys

input = sys.stdin.readline

def main():
    # input
    n = int(input())
    team_money, h_attack = map(int, input().split())
    
    attack = 0
    for _ in range(n):
        # input
        weapon_cost, weapon_attack = map(int, input().split())
        
        if team_money >= weapon_cost:
            attack = max(attack, weapon_attack)
    
    print('YES' if attack > h_attack else 'NO')

if __name__ == '__main__':
    main()