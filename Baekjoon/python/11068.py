# source : https://www.acmicpc.net/problem/11068

def main():
    # input
    t = int(input())
    nums = [int(input()) for _ in range(t)]
    
    [print(1) if isPalindrome(num) else print(0) for num in nums]
    
def isPalindrome(num: int) -> bool:
    for i in range(2, 65):
        is_palindrome = True
        temp = num
        
        nums = []
        while temp > 0:
            nums.append(temp % i)
            temp //= i
        
        for j in range(len(nums) // 2):
            if nums[j] != nums[-1 - j]:
                is_palindrome = False
                break    
            
        if is_palindrome:
            return is_palindrome
    
    return is_palindrome

if __name__ == '__main__':
    main()