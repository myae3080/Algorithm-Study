score_count = int(input())
score_list = list(map(int, input().split()))

total_score = 0

max_score = max(score_list)

for score in score_list:
    total_score += score

result_value = (total_score * 100) / (max_score * score_count)

print(round(result_value, 6))
