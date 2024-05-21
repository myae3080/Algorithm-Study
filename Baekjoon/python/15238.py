# source : https://www.acmicpc.net/problem/15238

from collections import defaultdict, Counter

def main():
    # input
    n = int(input())
    word = input()
    
    counts_by_chars = defaultdict(int)
    for c in word:
        counts_by_chars[c] += 1
    
    result = Counter(counts_by_chars).most_common()[0]
    
    print(result[0], result[1])

if __name__ == '__main__':
    main()