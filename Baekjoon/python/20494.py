# source : https://www.acmicpc.net/problem/20494

def main():
    result = 0
    
    # input
    for _ in range(int(input())):
        # input
        result += len(input())
    
    print(result)

if __name__ == '__main__':
    main()