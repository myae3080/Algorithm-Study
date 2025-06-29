# source : https://www.acmicpc.net/problem/31656

def main():
    # input
    sentence = input()
    
    result = ''
    for c in sentence:
        if not result or result[-1] != c:
            result += c
    
    print(result)

if __name__ == '__main__':
    main()