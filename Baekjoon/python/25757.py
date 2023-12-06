# source : https://www.acmicpc.net/problem/25757

def main():
    # input
    n, game = input().split()
    people = set([input() for _ in range(int(n))])
    
    if game == 'Y':
        print(len(people))
    elif game == 'F':
        print(len(people) // 2)
    else:
        print(len(people) // 3)

if __name__ == '__main__':
    main()