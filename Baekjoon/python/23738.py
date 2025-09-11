# source : https://www.acmicpc.net/problem/23738

def main():
    # input
    word = input()

    dic = {
        'A': 'a'
        , 'B': 'v'
        , 'E': 'ye'
        , 'H': 'n'
        , 'K': 'k'
        , 'M': 'm'
        , 'O': 'o'
        , 'P': 'r'
        , 'C': 's'
        , 'Y': 'u'
        , 'X': 'h'
        , 'T': 't'
    }

    print(''.join([dic[c] for c in word]))

if __name__ == '__main__':
    main()