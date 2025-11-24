# source : https://www.acmicpc.net/problem/5365

def main():
    # input
    n = int(input())
    sentence = input().split()

    result = sentence[0][0]
    for i in range(1, n):
        if len(sentence[i - 1]) > len(sentence[i]):
            result += ' '
        else:
            result += sentence[i][len(sentence[i - 1]) - 1]
    
    print(result)

if __name__ == '__main__':
    main()