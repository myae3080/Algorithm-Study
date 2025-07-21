# source : https://www.acmicpc.net/problem/32684

def main():
    pts = [13, 7, 5, 3, 3, 2]
    
    # input
    cho, han = list(map(int, input().split())), list(map(int, input().split()))
    
    cho_pts = sum([pts[i] * cho[i] for i in range(len(pts))])
    han_pts = sum([pts[i] * han[i] for i in range(len(pts))]) + 1.5
    
    if cho_pts > han_pts:
        print('cocjr0208')
    else:
        print('ekwoo')

if __name__ == '__main__':
    main()