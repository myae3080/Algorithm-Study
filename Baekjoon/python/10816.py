# data structure, binary search, Counter

'''
    TODO 이분 탐색을 이용한 풀이로 해결해보기
'''

'''
    첫 번째 풀이.
    이분 탐색을 시도했지만, 시간 초과에 막혀서 Counter class를 이용하여 푸는 방법으로 먼저 해결.
'''
import sys
from collections import Counter

# input
input = sys.stdin.readline

n = int(input())
count_dic = Counter((list(map(int, input().split()))))
m = int(input())
count_card_list = list(map(int, input().split()))

result_list = [0] * m

for i in range(m):
    result_list[i] = count_dic[count_card_list[i]]

[print(c, end=' ') for c in result_list]