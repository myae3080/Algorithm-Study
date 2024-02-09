# source : https://www.acmicpc.net/problem/23246

def main():
    rank_infos = []
    
    # input
    for _ in range(int(input())):
        # input
        back_number, p, q, r = map(int, input().split())
        
        rank_infos.append((p * q * r, p + q + r, back_number))
    
    rank_infos.sort(key=lambda tu: (tu[0], tu[1], tu[2]))
    
    for i in range(3):
        print(rank_infos[i][2], end=' ')

if __name__ == '__main__':
    main()