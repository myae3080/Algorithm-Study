# source : https://www.acmicpc.net/problem/2484

result = 0
for _ in range(int(input())):
    # input
    points = list(map(int, input().split()))
    
    dice = {}
    for point in points:
        if point in dice:
            dice[point] += 1
        else:
            dice[point] = 1
    
    size = len(dice)
    keys = list(dice.keys())
    if size == 1:
        result = max(result, 50000 + keys[0] * 5000)
    elif size == 4:
        result = max(result, max(keys) * 100)
    elif size == 3:
        for key in keys:
            if dice[key] == 2:
                result = max(result, 1000 + key * 100)
    else:
        if 3 in dice.values():
            for key in keys:
                if dice[key] == 3:
                    result = max(result, 10000 + key * 1000)
        else:
            result = max(result, 2000 + keys[0] * 500 + keys[1] * 500)

print(result)