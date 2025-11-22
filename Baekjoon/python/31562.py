# source : https://www.acmicpc.net/problem/31562

import sys

input = sys.stdin.readline

def main():
    # input
    N, M = map(int, input().split())
    
    songs = []
    for _ in range(N):
        # input
        inputs = input().split()

        T, S = inputs[0], inputs[1]

        songs.append((S, ''.join(inputs[2:])))
    
    for _ in range(M):
        # input
        names = ''.join(input().split())
        
        cnt = 0
        s = ''
        for song in songs:
            if names == song[1][:3]:
                cnt += 1
                s = song[0]
        
        if cnt == 0:
            print('!')
        elif cnt == 1:
            print(s)
        else:
            print('?')

if __name__ == '__main__':
    main()