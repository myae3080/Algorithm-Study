# source : https://www.acmicpc.net/problem/26004

def main():
    # input
    n = int(input())
    string = input()
    
    print(min(string.count('H'), string.count('I'), string.count('A'), string.count('R'), string.count('C')))

if __name__ == '__main__':
    main()