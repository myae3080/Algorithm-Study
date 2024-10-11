# source : https://www.acmicpc.net/problem/31428

def main():
    # input
    N = int(input())
    friends_track = list(input().split())
    hellobit_track = input()

    print(friends_track.count(hellobit_track))

if __name__ == '__main__':
    main()