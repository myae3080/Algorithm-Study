# source : https://www.acmicpc.net/problem/17350

def main():
    # input
    n = int(input())
    names = [input() for _ in range(n)]
    
    print('뭐야;') if names.count('anj') else print('뭐야?')
    
if __name__ == '__main__':
    main()