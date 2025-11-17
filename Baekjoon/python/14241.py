# source : https://www.acmicpc.net/problem/14241

def main():
    # input
    N = int(input())
    slimes = sorted(list(map(int, input().split())), reverse=True)

    slime = slimes[0]
    result = 0
    for i in range(1, N):
        result += slime * slimes[i]
        slime += slimes[i]
    
    print(result)

if __name__ == '__main__':
    main()