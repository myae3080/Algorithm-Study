# source : https://www.acmicpc.net/problem/9546

for _ in range(int(input())):
    count = 0
    # input
    for i in range(int(input())):
        count += 0.5
        count *= 2
    
    print(int(count))