# source : https://www.acmicpc.net/problem/2018

def main():
    # input
    n = int(input())
    
    start, end, sum = 1, 1, 1
    # n 자신의 수는 기본으로 count
    result = 1
    while end < n:
        if sum < n:
            end += 1
            sum += end
        elif sum > n:
            sum -= start
            start += 1
        else:
            result += 1
            end += 1
            sum += end
    
    print(result)

if __name__ == '__main__':
    main()