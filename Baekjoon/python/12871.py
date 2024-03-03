# source : https://www.acmicpc.net/problem/12871

def main():
    # input
    s, t = input(), input()
    
    print(1 if t * len(s) == s * len(t) else 0)

if __name__ == '__main__':
    main()