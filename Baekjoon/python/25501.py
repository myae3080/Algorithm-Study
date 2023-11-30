# source : https://www.acmicpc.net/problem/25501

def main():
    # input
    for _ in range(int(input())):
        # input
        word = input()
        
        is_palindrome = True
        count = 0
        for i in range(len(word) // 2 + 1):
            count += 1
            
            if word[i] != word[len(word) - i - 1]:
                is_palindrome = False
                break
        
        print(1 if is_palindrome else 0, count)

if __name__ == '__main__':
    main()