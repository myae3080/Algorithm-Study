# source : https://www.acmicpc.net/problem/25495

def main():
    # input
    N = int(input())
    phones = list(map(int, input().split()))
    
    result = 2
    prev = 2
    for i in range(1, N):
        if result != 0 and phones[i - 1] == phones[i]:
            consumption = prev * 2
            result += consumption
            prev = consumption
        else:
            result += 2
            prev = 2
        
        if result >= 100:
            result = 0
    
    print(result)

if __name__ == '__main__':
    main()