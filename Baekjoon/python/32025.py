# source : https://www.acmicpc.net/problem/32025

def main():
    # input
    H, W = int(input()), int(input())
    
    print(min(H, W) * 100 // 2)

if __name__ == '__main__':
    main()