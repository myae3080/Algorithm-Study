# source : https://www.acmicpc.net/problem/15947

def main():
    # input
    N = int(input())
    
    lyrics = ['baby', 'sukhwan', 'tururu', 'turu', 'very', 'cute', 'tururu', 'turu', 'in', 'bed', 'tururu', 'turu', 'baby', 'sukhwan']
    cycle = N // len(lyrics)
    
    lyric = lyrics[N % len(lyrics) - 1]
    if 'turu' in lyric:
        new_lyric = lyric + ('ru' * cycle)
        if new_lyric.count('ru') >= 5:
            print('tu+ru*%d' % new_lyric.count('ru'))
        else:
            print(new_lyric)
    else:
        print(lyric)

if __name__ == '__main__':
    main()