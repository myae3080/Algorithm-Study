# source : https://www.acmicpc.net/problem/26068

def main():
    # input
    n = int(input())
    print(len([1 for _ in range(n) if int(input()[2:]) <= 90]))
    
if __name__ == '__main__':
    main()