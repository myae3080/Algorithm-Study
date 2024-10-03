# source : https://www.acmicpc.net/problem/15874

def main():
    # input
    k, s = map(int, input().split())
    sentence = input()
    
    k %= 26
    result = ''
    for char in sentence:
        if char not in [' ', ',', '.']:
            if char.isupper():
                if ord(char) + k > ord('Z'):
                    result += chr(ord(char) + k - 26)
                else:
                    result += chr(ord(char) + k)
            else:
                if ord(char) + k > ord('z'):
                    result += chr(ord(char) + k - 26)
                else:
                    result += chr(ord(char) + k)
        else:
            result += char
    
    print(result)

if __name__ == '__main__':
    main()