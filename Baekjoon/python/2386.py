# source : https://www.acmicpc.net/problem/2386
# string, brute forcing

while True:
    # input
    input_str = input()

    if input_str == '#':
        break
    else:
        count = 0
        target = input_str[0]
        sentence = input_str[2:]

        for s in sentence:
            if s.lower() == target:
                count += 1

        print(target, count)