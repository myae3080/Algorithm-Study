# source : https://www.acmicpc.net/problem/15151

def main():
    # input
    k, d = map(int, input().split())
    
    book = 0
    while d > 0:
        days = k
        if d >= days:
            d -= days
        else:
            break
        
        book += 1
        k *= 2
    
    print(book)

if __name__ == '__main__':
    main()