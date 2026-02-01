# source : https://www.acmicpc.net/problem/9771

def main():
    # input
    word = input()

    result = 0
    while 1:
        try:
            # input
            s = input()

            result += s.count(word)
        except:
            break
    
    print(result)

if __name__ == '__main__':
    main()