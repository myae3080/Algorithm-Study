# source : https://www.acmicpc.net/problem/16462

import math

def main():
    # input
    n = int(input())
    
    scores = []
    for _ in range(n):
        # input
        score = input()
        
        scores.append(100 if score == '100' else int(score.replace('0', '9').replace('6', '9')))
    
    average = sum(scores) / n
    
    print(math.ceil(average) if average - int(average) >= 0.5 else int(average))

if __name__ == '__main__':
    main()