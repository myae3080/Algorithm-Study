# source : https://www.acmicpc.net/problem/25707

def main():
    # input
    n = int(input())
    beads = list(map(int, input().split()))

    beads.sort()

    result = 0
    for i in range(n):
        result += abs(beads[i] - beads[i - 1])
    
    print(result)

if __name__ == '__main__':
    main()