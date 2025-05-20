# source : https://www.acmicpc.net/problem/33779

def main():
    # input
    word = input()
    
    if word == word[::-1]:
        print('beep')
    else:
        print('boop')

if __name__ == '__main__':
    main()