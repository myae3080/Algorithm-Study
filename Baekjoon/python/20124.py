# source : https://www.acmicpc.net/problem/20124

def main():
    # input
    n = int(input())
    candidates = [(input().split()) for _ in range(n)]
    
    candidates.sort(key = lambda tu: (-int(tu[1]), tu[0]))
    
    print(candidates[0][0])
    
if __name__ == '__main__':
    main()