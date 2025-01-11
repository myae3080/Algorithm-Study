# source : https://www.acmicpc.net/problem/2508

def main():
    # input
    for _ in range(int(input())):
        # input
        input()
        r, c = map(int, input().split())
        box = [list(input()) for _ in range(r)]
        
        candies = 0
        for i in range(r):
            for j in range(c):
                # >o<
                if box[i][j] == '>':
                    if j + 2 < c:
                        if box[i][j + 1] == 'o' and box[i][j + 2] == '<':
                            candies += 1
                # v
                # o
                # ^
                if box[i][j] == 'v':
                    if i + 2 < r:
                        if box[i + 1][j] == 'o' and box[i + 2][j] == '^':
                            candies += 1
        
        print(candies)

if __name__ == '__main__':
    main()