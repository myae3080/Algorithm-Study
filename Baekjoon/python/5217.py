# source : https://www.acmicpc.net/problem/5217

# input
cases = sorted([int(input()) for _ in range(int(input()))])

for case in cases:
    prev = 1
    pairs = []

    while True:
        next = case - prev
        if prev >= next:
            break
        else:
            pairs.append([str(prev), str(next)])
            prev += 1
    
    print('Pairs for ' + str(case) + ': ', end='')
    if pairs:
        for i, pair in enumerate(pairs):
            if i == len(pairs) - 1:
                print(' '.join(pair))
            else:
                print(' '.join(pair), end=', ')
    else:
        print()