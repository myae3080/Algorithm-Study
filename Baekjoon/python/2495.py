# source : https://www.acmicpc.net/problem/2495

for _ in range(3):
    # input
    number = input()
    
    count, result = 0, 0
    prev = ''
    for n in number:
        if not prev:
            prev = n
            count = 1
        else:
            if prev == n:
                count += 1
            else:
                prev = n
                count = 1
                
        result = max(result, count)
                
    print(result)