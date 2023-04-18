# source : https://www.acmicpc.net/problem/17010

def main():
    # input
    for _ in range(int(input())):
        n, c = input().split()
        
        print(int(n) * c)

if __name__ == '__main__':
    main()