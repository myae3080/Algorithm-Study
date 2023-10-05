# source : https://www.acmicpc.net/problem/2703

def main():
    # input
    for _ in range(int(input())):
        # input
        message = input()
        rule = input()
        
        result = ''
        for m in message:
            idx = ord(m) - 65
            
            if idx >= 0:
                result += rule[idx]
            else:
                result += ' '

        print(result)

if __name__ == '__main__':
    main()