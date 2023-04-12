# source : https://www.acmicpc.net/problem/4299

def main():
    # input
    s, d = map(int, input().split())
    
    if s < d:
        print(-1)
    else:
        score1 = (s + d) // 2
        score2 = (s - d) // 2
        
        if (score1 + score2) == s and score1 - score2 == d:
            print(score1, score2)
        else:
            print(-1)
    
if __name__ == '__main__':
    main()