# source : https://www.acmicpc.net/problem/15128

def main():
    # input
    p1, q1, p2, q2 = map(int, input().split())
    
    s = (p1 * p2) / q1 / q2 / 2
    
    print(1 if s == int(s) else 0)

if __name__ == '__main__':
    main()