# source : https://www.acmicpc.net/problem/3230

def main():
    # input
    n, m = map(int, input().split())
    
    # 첫 번째 경주
    first_ranks = [0]
    for i in range(1, n + 1):
        # input
        first_ranks.insert(int(input()), i)
        
    # 두 번째 경주
    second_ranks = [0]
    for i in range(m, 0, -1):
        # input
        second_ranks.insert(int(input()), first_ranks[i])
    
    for player in second_ranks[1:4]:
        print(player)

if __name__ == '__main__':
    main()