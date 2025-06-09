# source : https://www.acmicpc.net/problem/20833

def main():
    # input
    N = int(input())
    
    print(sum([n ** 3 for n in range(1, N + 1)]))

if __name__ == '__main__':
    main()