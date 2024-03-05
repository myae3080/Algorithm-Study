# source : https://www.acmicpc.net/problem/28464

def main():
    # input
    n = int(input())
    fries = sorted(list(map(int, input().split())))
    
    half_idx = n // 2
    
    print(sum(fries[:half_idx]), sum(fries[half_idx:]))

if __name__ == '__main__':
    main()