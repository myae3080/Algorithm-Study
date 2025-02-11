# source : https://www.acmicpc.net/problem/6889

def main():
    # input
    n, m = int(input()), int(input())
    adjectives = [input() for _ in range(n)]
    nouns = [input() for _ in range(m)]
    
    for ad in adjectives:
        for noun in nouns:
            print(ad + ' as ' + noun)

if __name__ == '__main__':
    main()