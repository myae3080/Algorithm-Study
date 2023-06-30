# source : https://www.acmicpc.net/problem/2993

def main():
    # input
    word: str = input()
    
    result: str = word
    for i in range(1, len(result)):
        for j in range(i + 1, len(result)):
            combined_word = word[:i][::-1] + word[i:j][::-1] + word[j:][::-1]
            if result > combined_word:
                result = combined_word
    
    print(result)

if __name__ == '__main__':
    main()