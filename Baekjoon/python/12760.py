# source : https://www.acmicpc.net/problem/12760

def main():
    # input
    n, m = map(int, input().split())
    players = [sorted(list(map(int, input().split())), reverse=True) for _ in range(n)]
    
    scores = [0] * n
    for i in range(m):
        curr_round = [players[j][i] for j in range(n)]
        
        max_point = max(curr_round)
        for k in range(n):
            if curr_round[k] == max_point:
                scores[k] += 1
                
    max_score = max(scores)
    result = []
    for i in range(n):
        if scores[i] == max_score:
            result.append(i + 1)
    
    print(*result)

if __name__ == '__main__':
    main()