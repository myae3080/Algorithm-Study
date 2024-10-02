# source : https://www.acmicpc.net/problem/6750

def main():
    # input
    word = input()
    
    for c in word:
        if c not in ['I', 'O', 'S', 'H', 'Z', 'X', 'N']:
            print('NO')
            return
    
    print('YES')

if __name__ == '__main__':
    main()