# source : https://www.acmicpc.net/problem/31712

def main():
    # input
    skill_infos = sorted([list(map(int, input().split())) for _ in range(3)])
    hp = int(input())
    
    hp -= sum([info[1] for info in skill_infos])
    
    sec = 0
    while hp > 0:
        sec += 1
        
        for info in skill_infos:
            if sec % info[0] == 0:
                hp -= info[1]
        
        if hp <= 0:
            break
    
    print(sec)

if __name__ == '__main__':
    main()