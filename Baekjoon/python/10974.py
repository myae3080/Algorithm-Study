# source : https://www.acmicpc.net/problem/10974

from itertools import permutations

def main():
    # input
    n = int(input())
    
    for tu in list(permutations([i for i in range(1, n + 1)], n)):
        print(" ".join(map(str, tu)))

if __name__ == '__main__':
    main()