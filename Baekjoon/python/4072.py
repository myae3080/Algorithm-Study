# source : https://www.acmicpc.net/problem/4072

def main():
    while 1:
        # input
        words = input().split()
        
        if words[0] == '#':
            break
        
        for i in range(len(words)):
            words[i] = words[i][::-1]
        
        print(' '.join(words))

if __name__ == '__main__':
    main()