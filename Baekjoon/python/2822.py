# sorting

score_list = []
problem_list = []
sum = 0

# input
for i in range(1, 9):
    score_list.append((i, int(input())))

# sorting
score_list.sort(reverse=True, key=lambda t: t[1])

for i in range(5):
    tup = score_list[i]

    problem_list.append(tup[0])
    sum += tup[1]

# sorting
problem_list.sort()

print(sum)

for i in range(5):
    print(problem_list[i]) if i == 4 else print(problem_list[i], end=' ')