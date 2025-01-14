# source : https://www.acmicpc.net/problem/2756

def main():
    # input
    for _ in range(int(input())):
        # input
        scores = list(map(float, input().split()))
        
        N, M = 0, 0
        
        for i in range(6):
            if i <= 2:
                N += calculateScore(scores[2 * i] ** 2 + scores[2 * i + 1] ** 2)
            else:
                M += calculateScore(scores[2 * i] ** 2 + scores[2 * i + 1] ** 2)
        
        print('SCORE: %d to %d, %s.' % (N, M, 'PLAYER 1 WINS' if N > M else 'TIE' if N == M else 'PLAYER 2 WINS'))
    
def calculateScore(num: int) -> int:
    if num <= 9:
        return 100
    elif num <= 36:
        return 80
    elif num <= 81:
        return 60
    elif num <= 144:
        return 40
    elif num <= 225:
        return 20
    else:
        return 0

if __name__ == '__main__':
    main()