# data structure, string, sorting

import sys

# input
n, m = map(int, input().split())

no_hear_list = [sys.stdin.readline().rstrip() for i in range(n)]
no_see_list = [sys.stdin.readline().rstrip() for i in range(m)]

result_list = list(set(no_hear_list).intersection(no_see_list))

print(len(result_list))
# 사전순으로 정렬되지 않는 경우가 생김 -> sorted 필요
[print(s) for s in sorted(result_list)]