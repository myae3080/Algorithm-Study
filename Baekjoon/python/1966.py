# source : https://www.acmicpc.net/problem/1966
# data structure, queue

from collections import deque

for _ in range(int(input())):
    # input
    n, doc_idx = map(int, input().split())
    priorities = deque(map(int, input().split()))

    # 해당 문서 위치 deque
    locations = deque([0 for _ in range(n)])
    locations[doc_idx] = 1
    order = 0
    
    while True:
        if  priorities[0] == max(priorities):
            order += 1
            
            if locations[0] == 1:
                print(order)
                break
            else:
                priorities.popleft()
                locations.popleft()
        else:
            priorities.append(priorities.popleft())
            locations.append(locations.popleft())