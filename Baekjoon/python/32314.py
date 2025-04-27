# source : https://www.acmicpc.net/problem/32314

def main():
    # input
    a = int(input())
    w, v = map(int, input().split())

    print(1 if w // v >= a else 0)

if __name__ == '__main__':
    main()