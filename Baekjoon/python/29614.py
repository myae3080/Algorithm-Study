# source : https://www.acmicpc.net/problem/29614

def main():
    scores_by_ranks = {
        'A+': 4.5, 'A': 4,
        'B+': 3.5, 'B': 3,
        'C+': 2.5, 'C': 2,
        'D+': 1.5, 'D': 1,
        'F': 0
    }
    
    # input
    ranks = input()
    
    result = 0
    cnt = 0
    has_plus = False
    for i in range(len(ranks) - 1, -1, -1):
        if ranks[i] == '+':
            has_plus = True
        else:
            if has_plus:
                result += scores_by_ranks[ranks[i] + '+']
            else:
                result += scores_by_ranks[ranks[i]]
            
            has_plus = False
            cnt += 1
    
    print(float("{:.5f}".format(result / cnt)))
        
if __name__ == '__main__':
    main()