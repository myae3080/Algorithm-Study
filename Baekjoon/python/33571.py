# source : https://www.acmicpc.net/problem/33571

def main():
    holes_by_char = {
        'A': 1, 'a': 1
        , 'B': 2, 'b': 1
        , 'D': 1, 'd': 1
        , 'e': 1, 'g': 1
        , 'O': 1, 'o': 1
        , 'P': 1, 'p': 1
        , 'Q': 1, 'q': 1
        , 'R': 1
        , '@': 1
    }
    
    result = 0
    
    # input
    for c in input():
        if c in holes_by_char:
            result += holes_by_char[c]
    
    print(result)

if __name__ == '__main__':
    main()