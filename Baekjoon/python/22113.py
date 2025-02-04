# source : https://www.acmicpc.net/problem/22113

def main():
    # input
    N, M = map(int, input().split())
    bus_number = list(map(int, input().split()))
    bus_fare = [list(map(int, input().split())) for _ in range(N)]
    
    result = 0
    for i in range(1, M):
        result += bus_fare[bus_number[i - 1] - 1][bus_number[i] - 1]
    
    print(result)

if __name__ == '__main__':
    main()