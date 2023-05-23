# source : https://www.acmicpc.net/problem/26546

def main():
    # input
    t = int(input())
    for _ in range(t):
        # input
        word, i, j = input().split()
        
        print(word[:int(i)] + word[int(j):])

if __name__ == '__main__':
    main()