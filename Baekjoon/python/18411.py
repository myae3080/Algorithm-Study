# source : https://www.acmicpc.net/problem/18411

def main():
    # input
    print(sum(sorted(list(map(int, input().split())), reverse=True)[:2]))
    
if __name__ == '__main__':
    main()