# source : https://www.acmicpc.net/problem/16495

def main():
    # input
    word = input()
    
    result = 0
    for i in range(len(word)):
        result += (ord(word[i]) - 64) * (26 ** (len(word) - i - 1))
    
    print(result)

if __name__ == '__main__':
    main()