# source : https://www.acmicpc.net/problem/11507

def main():
    # input
    s = input()

    cards = [s[i:i + 3] for i in range(0, len(s), 3)]

    if len(set(cards)) != len(cards):
        print('GRESKA')
    else:
        cards_count = {'P': 13, 'K': 13, 'H': 13, 'T': 13}
        for c in cards:
            cards_count[c[0]] -= 1
        
        print(' '.join([str(n) for n in cards_count.values()]))

if __name__ == '__main__':
    main()