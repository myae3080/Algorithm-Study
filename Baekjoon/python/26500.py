# source : https://www.acmicpc.net/problem/26500

def main():
    # input
    for _ in range(int(input())):
        # input
        a, b = map(float, input().split())
        
        print(round(abs(a - b), 1))

if __name__ == '__main__':
    main()