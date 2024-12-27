# source : https://www.acmicpc.net/problem/32866

def main():
    # input
    N, X = int(input()), int(input())
    
    loss = N * (100 - X) / 100
    
    print(round((N / loss) * 100 - 100, 6))

if __name__ == '__main__':
    main()