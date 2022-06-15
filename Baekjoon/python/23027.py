# source : https://www.acmicpc.net/problem/23027

# input
S = input()

has_A = 'A' in S
has_B = 'B' in S
has_C = 'C' in S

if has_A:
    print(S.replace('B', 'A').replace('C', 'A').replace('D', 'A').replace('F', 'A'))
else:
    if has_B:
        print(S.replace('C', 'B').replace('D', 'B').replace('F', 'B'))
    else:
        if has_C:
            print(S.replace('D', 'C').replace('F', 'C'))
        else:
            print('A' * len(S))