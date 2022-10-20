# source : https://www.acmicpc.net/problem/4641

while 1:
    # input
    li = list(map(int, input().split()))[:-1]
    
    if len(li) == 0:
        break
    
    result = 0
    for n in li:
        double = n * 2
        if li.count(double) > 0:
            result += 1
    
    print(result)