# source : https://www.acmicpc.net/problem/27890

def main():
    # input
    a, b = map(int, input().split())
    
    for _ in range(b):
        a = (a // 2) ^ 6 if a % 2 == 0 else (a * 2) ^ 6
            
    print(a)

if __name__ == '__main__':
    main()