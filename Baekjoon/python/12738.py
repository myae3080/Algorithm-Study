# source : https://www.acmicpc.net/problem/12738

def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))
    
    result = [A[0]]
    for i in range(1, N):
        if result[-1] < A[i]:
            result.append(A[i])
        else:
            target_idx = binary_search(result, A[i])
            result[target_idx] = A[i]
        
    print(len(result))

def binary_search(arr: list, target: int) -> int:
    left, right = 0, len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return left

if __name__ == '__main__':
    main()