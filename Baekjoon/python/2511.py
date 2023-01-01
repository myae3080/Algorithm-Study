# source : https://www.acmicpc.net/problem/2511

# input
a_cards, b_cards = list(map(int, input().split())), list(map(int, input().split()))

a_scores, b_scores = 0, 0
is_all_draw, is_a = True, True

for i in range(len(a_cards)):
    if a_cards[i] == b_cards[i]:
        a_scores += 1
        b_scores += 1
    else:
        is_all_draw = False
        if a_cards[i] > b_cards[i]:
            a_scores += 3
            is_a = True
        else:
            b_scores += 3
            is_a = False

print(a_scores, b_scores)
if a_scores == b_scores:
    print('D') if is_all_draw else print('A') if is_a else print('B')
else:
    print('A') if a_scores > b_scores else print('B')