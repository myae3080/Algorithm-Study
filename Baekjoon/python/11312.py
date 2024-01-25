# source : https://www.acmicpc.net/problem/11312

def main():
    # input
    for _ in range(int(input())):
        # input
        a, b = map(int, input().split())
        
        print((a // b) ** 2)

if __name__ == '__main__':
    main()