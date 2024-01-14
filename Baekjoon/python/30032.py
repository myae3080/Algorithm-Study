# source : https://www.acmicpc.net/problem/30032

def main():
    dic = {
        '1': {
            'd': 'q',
            'b': 'p',
            'q': 'd',
            'p': 'b'
        },
        '2': {
            'd': 'b',
            'b': 'd',
            'q': 'p',
            'p': 'q'
        }
    }
    
    # input
    n, d = map(int, input().split())
    alphabet = [input() for _ in range(n)]
    
    for al in alphabet:
        result = ''
        for c in al:
            result += dic[str(d)][c]
        
        print(result)

if __name__ == '__main__':
    main()