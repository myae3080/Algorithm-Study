# source : https://www.acmicpc.net/problem/18398

def main():
    # input
    for _ in range(int(input())):
        # input
        for __ in range(int(input())):
            # input
            a, b = map(int, input().split())
            
            print(a + b, a * b)

if __name__ == '__main__':
    main()