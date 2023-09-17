# source : https://www.acmicpc.net/problem/11008

def main():
    # input
    n = int(input())
    
    for _ in range(n):
        # input
        word, copy = input().split()
        
        cnt = word.count(copy)
        
        print(len(word) - (len(copy) * cnt) + cnt)

if __name__ == '__main__':
    main()