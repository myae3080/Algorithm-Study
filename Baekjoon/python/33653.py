# source : https://www.acmicpc.net/problem/33653

def main():
    # input
    W = input()
    M = int(input())
    words = list(input().split())
    
    result = 0
    for word in words:
        if len(word) > len(W):
            for i in range(len(word) - len(W) + 1):
                if word[i:i + len(W)] == W:
                    result += 1
        else:
            if word == W:
                result += 1
    
    print(result)

if __name__ == '__main__':
    main()