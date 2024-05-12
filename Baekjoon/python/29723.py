# source : https://www.acmicpc.net/problem/29723

def main():
    # input
    n, m, k = map(int, input().split())
    
    scores_by_subjects = {}
    for _ in range(n):
        # input
        subject, score = input().split()
        
        scores_by_subjects[subject] = int(score)
    
    score = 0
    for _ in range(k):
        # input
        subject = input()
        
        score += scores_by_subjects[subject]
        
        del scores_by_subjects[subject]
        
    sorted_scores = sorted(scores_by_subjects.values())
    min_score, max_score = 0, 0
    for i in range(m - k):
        min_score += sorted_scores[i]
        max_score += sorted_scores[-i - 1]
        
    print(score + min_score, score + max_score)

if __name__ == '__main__':
    main()