# sorting

w_score = []
k_score = []

# input
[w_score.append(int(input())) if i < 10 else k_score.append(int(input())) for i in range(20)]

w_score.sort(reverse=True)
k_score.sort(reverse=True)

print(sum(w_score[:3]), sum(k_score[:3]))