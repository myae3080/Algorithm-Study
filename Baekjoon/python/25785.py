# source : https://www.acmicpc.net/problem/25785

def main():
    # input
    word = input()
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    is_easy = True
    for i in range(len(word) - 1):
        if word[i] not in vowels and word[i + 1] not in vowels:
            is_easy = False
        if word[i] in vowels and word[i + 1] in vowels:
            is_easy = False
            
            break
    
    print(1 if is_easy else 0)

if __name__ == '__main__':
    main()