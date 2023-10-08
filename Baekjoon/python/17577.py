# source : https://www.acmicpc.net/problem/17577

def main():
    while 1:
        # input
        n, m = map(int, input().split())
        
        if n == m == 0:
            break
        
        # input
        datasets = [list(map(int, input().split())) for _ in range(m)]
        
        highest_score = 0
        for i in range(n):
            score = 0
            for j in range(m):
                score += datasets[j][i]
            
            highest_score = max(highest_score, score)
        
        print(highest_score)
        
if __name__ == '__main__':
    main()