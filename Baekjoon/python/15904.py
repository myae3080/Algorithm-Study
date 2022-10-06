# source : https://www.acmicpc.net/problem/15904

# input
sentence = input()
abbreviation = 'UCPC'
is_ucpc = True

for c in abbreviation:
    if c in sentence:
        sentence = sentence[sentence.find(c) + 1:]
    else:
        print('I hate UCPC')
        is_ucpc = False
        break

if is_ucpc:
    print('I love UCPC')