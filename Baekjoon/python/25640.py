# source : https://www.acmicpc.net/problem/25640

def main():
    # input
    mbti = input()
    mbtis = [input() for _ in range(int(input()))]
    
    print(mbtis.count(mbti))
    
if __name__ == '__main__':
    main()