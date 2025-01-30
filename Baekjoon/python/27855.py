# source : https://www.acmicpc.net/problem/27855

def main():
    # input
    h1, b1 = map(int, input().split())
    h2, b2 = map(int, input().split())
    
    p1_score = (h1 * 3) + b1
    p2_score = (h2 * 3) + b2
    
    if p1_score == p2_score:
        print('NO SCORE')
    else:
        print('%d %d' % (1 if p1_score > p2_score else 2, abs(p1_score - p2_score)))

if __name__ == '__main__':
    main()