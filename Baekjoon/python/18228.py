# source : https://www.acmicpc.net/problem/18228

def main():
    # input
    n = int(input())
    front, behind = input().split('-1')
    
    print(min(list(map(int, front.split()))) + min(list(map(int, behind.split()))))
    
if __name__ == '__main__':
    main()