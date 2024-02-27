# source : https://www.acmicpc.net/problem/23971

import math

def main():
    # input
    h, w, n, m = map(int, input().split())
    
    print(math.ceil(h / (n + 1)) * math.ceil(w / (m + 1)))

if __name__ == '__main__':
    main()