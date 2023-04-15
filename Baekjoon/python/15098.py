# source : https://www.acmicpc.net/problem/15098

def main():
    # input
    words = list(input().split())

    print('no') if len(words) != len(set(words)) else print('yes')
        
if __name__ == '__main__':
    main()