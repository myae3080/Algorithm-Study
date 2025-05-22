# source : https://www.acmicpc.net/problem/30156

def main():
    # input
    for _ in range(int(input())):
        # input
        s = input()
        
        print(min(s.count('a'), s.count('b')))

if __name__ == '__main__':
    main()