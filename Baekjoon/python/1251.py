# source : https://www.acmicpc.net/problem/1251

def main():
    # input
    word = input()
    
    length = len(word)
    words = []
    for i in range(1, length - 1):
        for j in range(i + 1, length):
            words.append(word[:i][::-1] + word[i:j][::-1] + word[j:][::-1])
            
    words.sort()
    print(words[0])

if __name__ == '__main__':
    main()