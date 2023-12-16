# source : https://www.acmicpc.net/problem/3076

def main():
    # input
    r, c = map(int, input().split())
    a, b = map(int, input().split())
    
    # col 구성
    even_row = ''
    for i in range(c):
        if i % 2 == 0:
            even_row += 'X' * b
        else:
            even_row += '.' * b
    
    odd_row = ''
    for i in range(c):
        if i % 2 == 0:
            odd_row += '.' * b
        else:
            odd_row += 'X' * b
    
    # row 구성
    for i in range(r):
        if i % 2 == 0:
            for _ in range(a):
                print(even_row)
        else:
            for _ in range(a):
                print(odd_row)

if __name__ == '__main__':
    main()