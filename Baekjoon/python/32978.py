# source : https://www.acmicpc.net/problem/32978

def main():
    # input
    N = int(input())
    ingredients = list(input().split())
    used = list(input().split())
    
    for i in used:
        ingredients.remove(i)
    
    print(*ingredients)

if __name__ == '__main__':
    main()