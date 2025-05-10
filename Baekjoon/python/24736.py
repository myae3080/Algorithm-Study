# source : https://www.acmicpc.net/problem/24736

def main():
    for _ in range(2):
        # input
        T, F, S, P, C = map(int, input().split())
        
        print(T * 6 + F * 3 + S * 2 + P + C * 2)

if __name__ == '__main__':
    main()