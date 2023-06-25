# source : https://www.acmicpc.net/problem/11970

def main():
    # input
    s1, e1 = map(int, input().split())
    s2, e2 = map(int, input().split())
    
    if e1 <= s2 or e2 <= s1:
        print((e1 - s1) + (e2 - s2))
    else:
        print(max(e1, e2) - min(s1, s2))
    
if __name__ == '__main__':
    main()