# source : https://www.acmicpc.net/problem/13301

def main():
    # input
    n = int(input())
    
    tiles = [0] * (n + 2)
    tiles[1] = 1
    
    for i in range(2, n + 2):
        tiles[i] = tiles[i - 1] + tiles[i - 2]
    
    print((tiles[n + 1] + tiles[n]) * 2)

if __name__ == '__main__':
    main()