# source : https://www.acmicpc.net/problem/28444

def main():
    # input
    H, I, A, R, C = map(int, input().split())
    
    print(H * I - A * R * C)

if __name__ == '__main__':
    main()