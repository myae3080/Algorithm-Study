# source : https://www.acmicpc.net/problem/14247

def main():
    # input
    n = int(input())
    heights = list(map(int, input().split()))
    rates = list(map(int, input().split()))

    trees = []
    for i in range(n):
        trees.append((rates[i], heights[i]))
    
    trees.sort()

    result = 0
    for i in range(n):
        result += (trees[i][1] + trees[i][0] * i)
    
    print(result)

if __name__ == '__main__':
    main()