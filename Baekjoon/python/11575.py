# source : https://www.acmicpc.net/problem/11575

def main():
    # input
    for _ in range(int(input())):
        # input
        a, b = map(int, input().split())
        word = input()
        
        print(''.join([chr(((a * (ord(c) - 65) + b) % 26) + 65) for c in word]))
            
if __name__ == '__main__':
    main()