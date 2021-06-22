# graph theory, graph search, dfs, bfs

import sys

'''
    컴퓨터를 오름차순으로 정렬을 해서 재방문에 대한 고려를 해결할 수 있을 줄 알았으나, 빠지는 부분이 생겨 정렬없이 세팅 후,
    1번 부터 다 뒤지는 방식으로 해결
'''
# input
input = sys.stdin.readline
com_count = int(input())

virus_dict = {}
visited_list = []

def check_com(start, visited):
    for j in virus_dict[start]:
        if j not in visited_list:
            visited.append(j)
            check_com(j, visited)

for i in range(1, 101):
    virus_dict[i] = set()

for i in range(int(input())):
    # input
    com1, com2 = map(int, input().rstrip().split())
    virus_dict[com1].add(com2)
    virus_dict[com2].add(com1)

check_com(1, visited_list)

print(len(visited_list) - 1)