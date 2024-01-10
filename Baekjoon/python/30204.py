# source : https://www.acmicpc.net/problem/30204

def main():
    # input
    n, x = map(int, input().split())
    people = list(map(int, input().split()))
    
    print(1 if sum(people) % x == 0 else 0)
    
if __name__ == '__main__':
    main()