# source : https://www.acmicpc.net/problem/15351

def main():
    for _ in range(int(input())):
        # input
        scores = sum([ord(c) - 64 for c in input().replace(' ', '')])
        
        print('PERFECT LIFE') if scores == 100 else print(scores)
        
if __name__ == '__main__':
    main()