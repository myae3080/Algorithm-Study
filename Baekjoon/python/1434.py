# source : https://www.acmicpc.net/problem/1434

def main():
    # input
    box, book = map(int, input().split())
    print(sum(list(map(int, input().split()))) - sum(list(map(int, input().split()))))

if __name__ == '__main__':
    main()