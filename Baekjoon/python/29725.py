# source : https://www.acmicpc.net/problem/29725

def main():
    pieces = {
        'k': 0
        , 'p': 1
        , 'n': 3
        , 'b': 3
        , 'r': 5
        , 'q': 9
    }
    
    b, w = 0, 0
    
    for _ in range(8):
        # input
        for p in list(input()):
            if p == '.':
                continue
            
            if p.islower():
                w += pieces[p.lower()]
            else:
                b += pieces[p.lower()]

    print(b - w)

if __name__ == '__main__':
    main()