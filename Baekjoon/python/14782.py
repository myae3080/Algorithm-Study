# source : https://www.acmicpc.net/problem/14782

def main():
    # input
    i = int(input())
    
    print(sum([n for n in range(1, i + 1) if i % n == 0]))

if __name__ == '__main__':
    main()