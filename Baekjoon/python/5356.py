# source : https://www.acmicpc.net/problem/5356

def main():
    # input
    for _ in range(int(input())):
        # input
        n, c = input().split()

        char = ord(c)
        for i in range(int(n)):
            print(chr(char) * (i + 1))

            if char == 90:
                char -= 25
            else:
                char += 1
        
        print()
            
if __name__ == '__main__':
    main()