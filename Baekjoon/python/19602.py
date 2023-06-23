# source : https://www.acmicpc.net/problem/19602

def main():
    print('happy') if sum([int(input()) * (i + 1) for i in range(3)]) >= 10 else print('sad')
    
if __name__ == '__main__':
    main()