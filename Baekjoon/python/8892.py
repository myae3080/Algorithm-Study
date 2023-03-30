# source : https://www.acmicpc.net/problem/8892

def main():
    # input
    for _ in range(int(input())):
        # input
        count = int(input())
        words = [input() for __ in range(count)]
        
        has_palindrome = False
        for i in range(count):
            for j in range(i + 1, count):
                combination1 = words[i] + words[j]
                combination2 = words[j] + words[i]
                
                if isPalindrome(combination1):
                    print(combination1)
                    has_palindrome = True
                    break
                
                if isPalindrome(combination2):
                    print(combination2)
                    has_palindrome = True
                    break
                
            if has_palindrome:
                break
            
        if not has_palindrome:
            print(0)

def isPalindrome(word: str) -> bool:
    length = len(word)
    half = length // 2
    for i in range(half):
        if word[i] != word[length - i - 1]:
            return False
        
    return True
    
if __name__ == '__main__':
    main()