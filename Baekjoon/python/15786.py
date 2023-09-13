# source : https://www.acmicpc.net/problem/15786

def main():
    # input
    n, m = map(int, input().split())
    word = input()
    postits = [input() for _ in range(m)]
    
    for postit in postits:
        qu = list(word)
        
        for c in postit:
            if len(qu) == 0:
                break
            
            if qu[0] == c:
                del qu[0]
        
        print('true') if len(qu) == 0 else print('false')

if __name__ == '__main__':
    main()