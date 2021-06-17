# sorting

import sys
from collections import Counter

# input
input = sys.stdin.readline

num_list = sorted([int(input()) for i in range(int(input()))])

# 산술평균
print(round(sum(num_list) / len(num_list)))
# 중앙값
print(num_list[len(num_list) // 2])
# 최빈값
counter = Counter(num_list).most_common()

if len(counter) == 1:
    print(counter[0][0])
else:
    print(counter[1][0]) if counter[0][1] == counter[1][1] else print(counter[0][0])
# 범위
print(num_list[-1] - num_list[0])