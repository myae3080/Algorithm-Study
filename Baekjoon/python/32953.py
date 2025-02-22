# source : https://www.acmicpc.net/problem/32953

def main():
    # input
    N, M = map(int, input().split())
    
    count_by_number = {}
    for _ in range(N):
        # input
        K = int(input())
        stu_nums = list(map(int, input().split()))
        
        for num in stu_nums:
            if num in count_by_number:
                count_by_number[num] += 1
            else:
                count_by_number[num] = 1
    
    result = 0
    for subjects in count_by_number.values():
        if subjects >= M:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()