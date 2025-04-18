# source : https://www.acmicpc.net/problem/17285

def main():
    # input
    T = input()
    
    key = ord(T[0]) ^ ord('C')
    result = ''
    for c in T:
        result += chr(ord(c) ^ key)
    
    print(result)

if __name__ == '__main__':
    main()