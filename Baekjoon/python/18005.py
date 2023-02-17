# source : https://www.acmicpc.net/problem/18005

def main():
    # input
    n = int(input())
    
    if n % 2 == 1:
        print(0)
    else:
        if (n // 2) % 2 == 1:
            print(1)
        else:
            print(2)
    
if __name__ == '__main__':
    main()