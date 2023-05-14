# source : https://www.acmicpc.net/problem/12778

def main():
    # input
    t = int(input())
    for _ in range(t):
        # input
        m, type = input().split()
        if type == 'C':
            q = list(input().split())
        else:
            q = list(map(int, input().split()))
            
        if type == 'C':
            [print(ord(c) - 64, end=' ') for c in q]
        else:
            [print(chr(n + 64), end=' ') for n in q]
        print()

if __name__ == '__main__':
    main()