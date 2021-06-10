# math

sum = 0

for i in range(5):
    score = int(input())

    sum += 40 if score < 40 else score

print(sum // 5)