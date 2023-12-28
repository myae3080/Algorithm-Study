# source : https://www.acmicpc.net/problem/1817

def main():
    # input
    n, m = map(int, input().split())
    
    if n == 0:
        print(0)
        return
    
    # input
    weights = list(map(int, input().split()))
    
    boxes = 1
    capa = m - weights[0]
    for i in range(1, n):
        book_weight = weights[i]
        
        if capa >= book_weight:
            capa -= book_weight
        else:
            boxes += 1
            capa = m - book_weight
    
    print(boxes)

if __name__ == '__main__':
    main()