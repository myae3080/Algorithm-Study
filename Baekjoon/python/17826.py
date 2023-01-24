# source : https://www.acmicpc.net/problem/17826

def main():
    # input
    scores = list(map(int, input().split()))
    hong_score = int(input())
    
    ranks = {
        5: 'A+',
        15: 'A0',
        30: 'B+',
        35: 'B0',
        45: 'C+',
        48: 'C0',
        50: 'F'
    }
    rank = scores.index(hong_score) + 1
    
    for k in ranks.keys():
        if rank <= k:
            print(ranks.get(k))
            break
        
if __name__ == '__main__':
    main()