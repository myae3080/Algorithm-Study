# source : https://www.acmicpc.net/problem/11034

def main():
    while 1:
        try:
            # input
            a, b, c = map(int, input().split())

            print(max(b - a, c - b) - 1)
        except EOFError:
            break
 
if __name__ == '__main__':
    main()