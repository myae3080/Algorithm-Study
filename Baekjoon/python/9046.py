# source : https://www.acmicpc.net/problem/9046

def main():
    # input
    for _ in range(int(input())):
        # input
        sentence = input()
        
        alpha = [0 for _ in range(26)]
        
        for c in sentence:
            if c != ' ':
                alpha[ord(c) - 97] += 1
        
        if alpha.count(max(alpha)) > 1:
            print('?')
        else:
            print(chr(alpha.index(max(alpha)) + 97))

if __name__ == '__main__':
    main()