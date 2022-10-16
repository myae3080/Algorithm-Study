# source : https://www.acmicpc.net/problem/6550

while True:
    try:
        # input
        word, origin = input().split()

        is_substring = True
        for c in word:
            target_idx = origin.find(c)
            if target_idx != -1:
                origin = origin[target_idx + 1:]
            else:
                is_substring = False
                print('No')
                break

        if is_substring:
            print('Yes')
    except:
        break