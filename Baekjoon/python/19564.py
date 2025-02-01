# source : https://www.acmicpc.net/problem/19564

def main():
    # input
    word = input()
    
    result = 1
    for i in range(1, len(word)):
        if ord(word[i]) <= ord(word[i - 1]):
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()