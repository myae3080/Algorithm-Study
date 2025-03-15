# source : https://www.acmicpc.net/problem/13772

def main():
    holes_by_char = {
        'A': 1, 'D': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1
        , 'B': 2
    }
    
    # input
    for _ in range(int(input())):
        # input
        text = input()
        
        result = 0
        for c in text:
            if c in holes_by_char:
                result += holes_by_char[c]
        
        print(result)

if __name__ == '__main__':
    main()