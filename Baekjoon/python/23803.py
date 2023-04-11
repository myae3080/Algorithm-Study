# source : https://www.acmicpc.net/problem/23803

def main():
    # input
    n = int(input())
    
    for _ in range(n * 4):
        print('@' * n)
    
    for _ in range(n):
        print('@' * 5 * n)
    
if __name__ == '__main__':
    main()