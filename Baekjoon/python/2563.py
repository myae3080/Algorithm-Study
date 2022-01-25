# source : https://www.acmicpc.net/problem/2563

points = set()
count = 0

for _ in range(int(input())):
    # input
    x, y = map(int, input().split())
    
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if (i, j) not in points:
                count += 1
                points.add((i, j))
                
print(count)