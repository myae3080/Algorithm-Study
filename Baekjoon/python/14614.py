# source : https://www.acmicpc.net/problem/14614

def main():
    # input
    a, b, c = map(int, input().split())
    
    print((a ^ b) ^ b if c % 2 == 0 else a ^ b)
    
if __name__ == '__main__':
    main()