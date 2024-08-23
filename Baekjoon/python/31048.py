# source : https://www.acmicpc.net/problem/31048

def main():
    # input
    for _ in range(int(input())):
        # input
        n = int(input())
        
        result = 1
        for i in range(1, n + 1):
            result = (result * i) % 10
        
        print(result)

if __name__ == '__main__':
    main()