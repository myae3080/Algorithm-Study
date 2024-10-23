# source : https://www.acmicpc.net/problem/31746

def main():
    # input
    N = int(input())
    
    word = 'SciComLove'
    
    print(word if N % 2 == 0 else word[::-1])

if __name__ == '__main__':
    main()