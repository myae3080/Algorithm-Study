# source : https://www.acmicpc.net/problem/11256

# input
for _ in range(int(input())):
    # input
    candy_count, box_count = map(int, input().split())
    
    capacities = []
    for __ in range(box_count):
        w, h = map(int, input().split())
        capacities.append(w * h)
        
    capacities.sort(reverse=True)
    
    result = 0
    for capa in capacities:
        result += 1
        candy_count -= capa
        if candy_count <= 0:
            print(result)
            break        