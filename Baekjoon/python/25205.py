# source : https://www.acmicpc.net/problem/25205

def main():
    # input
    N = int(input())
    s = input()
    
    medials = 'kijuhynbmlop'
    
    if s[-1] in medials:
        print(0)
    else:
        print(1)

if __name__ == '__main__':
    main()