# source : https://www.acmicpc.net/problem/7596

def main():
    count = 0
    while 1:
        # input
        n = int(input())
        
        if n == 0:
            break
        
        count += 1
        
        # input
        songs = sorted([input() for _ in range(n)])
        
        print(count)
        for song in songs:
            print(song)

if __name__ == '__main__':
    main()