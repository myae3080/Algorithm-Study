# source : https://www.acmicpc.net/problem/14592

def main():
    # input
    participants = [list(map(int, input().split())) for _ in range(int(input()))]
        
    rank = sorted(participants, key=lambda data:(-data[0], data[1], data[2]))
    
    print(participants.index(rank[0]) + 1)
    
if __name__ == '__main__':
    main()