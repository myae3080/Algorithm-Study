# source : https://www.acmicpc.net/problem/14696

for _ in range(int(input())):
    # input
    a, b = list(map(int, input().split()))[1:], list(map(int, input().split()))[1:]
    
    for i in range(4, 0, -1):
        a_count, b_count = a.count(i), b.count(i)
        
        if a_count > b_count:
            print('A')
            break
        elif a_count < b_count:
            print('B')
            break
        elif i == 1:
            print('D')