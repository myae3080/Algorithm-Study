# source : https://www.acmicpc.net/problem/4493

for _ in range(int(input())):
    p1, p2 = 0, 0
    
    for _ in range(int(input())):
        # input
        a, b = input().split()
        
        if a == b:
            continue
        else:
            if (a == 'R' and b == 'S') or (a == 'S' and b == 'P') or (a == 'P' and b == 'R'):
                p1 += 1
            else:
                p2 += 1
    
    print('TIE') if p1 == p2 else print('Player 1') if p1 > p2 else print('Player 2')