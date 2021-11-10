# source : https://www.acmicpc.net/problem/7795
# sorting, binary search, two pointers

for _ in range(int(input())):
    # input
    a_count, b_count = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())), reverse=True)
    
    count = 0
    
    for num in a:
        start, end = 0, b_count - 1
        result = 0
        
        while start <= end:
            mid = (start + end) // 2
            
            if b[mid] < num:
                end = mid - 1
            else:
                start = mid + 1
                result = mid + 1
                
        # 기존 소스 len(b[result:]) 로 했을 시, 100%에서 시간초과 뜸.
        count += b_count - result
    
    print(count)