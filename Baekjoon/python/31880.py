# source : https://www.acmicpc.net/problem/31880

def main():
    # input
    N, M = map(int, input().split())
    a_books = list(map(int, input().split()))
    b_books = list(map(int, input().split()))
    
    a_luck = sum(a_books)
    b_luck = 1
    for b in b_books:
        if b != 0:
            b_luck *= b

    print(a_luck * b_luck)

if __name__ == '__main__':
    main()