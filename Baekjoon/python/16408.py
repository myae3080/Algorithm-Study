# source : https://www.acmicpc.net/problem/16408

def main():
    rank_by_key = {}
    for c in 'A23456789TJQK':
        rank_by_key[c] = 0
    
    # input
    cards = input().split()
    
    for card in cards:
        rank_by_key[card[0]] += 1
    
    print(max(rank_by_key.values()))

if __name__ == '__main__':
    main()