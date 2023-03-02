# source : https://www.acmicpc.net/problem/14724

def main():
    club = ['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']
    
    # input
    n = int(input())
    representatives = [max(list(map(int, input().split()))) for i in range(len(club))]
    
    print(club[representatives.index(max(representatives))])    

if __name__ == '__main__':
    main()