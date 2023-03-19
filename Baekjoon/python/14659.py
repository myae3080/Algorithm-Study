# source : https://www.acmicpc.net/problem/14659

def main():
    # input
    n = int(input())
    peaks = list(map(int, input().split()))
    
    max_peak = 0
    result, temp = 0, 0
    for i in range(n):
        if max_peak > peaks[i]:
            temp += 1
        else:
            max_peak = peaks[i]
            result = max(result, temp)
            temp = 0
            
    result = max(result, temp)
    
    print(result)
    
if __name__ == '__main__':
    main()