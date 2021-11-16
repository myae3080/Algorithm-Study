# source : https://www.acmicpc.net/problem/5532
# math

# input
days, korean_pages, math_pages, korean_per_day, math_per_day = int(input()), int(input()), int(input()), int(input()), int(input())

k = korean_pages // korean_per_day if korean_pages % korean_per_day == 0 else korean_pages // korean_per_day + 1
m = math_pages // math_per_day if math_pages % math_per_day == 0 else math_pages // math_per_day + 1

print(days - max(k, m))