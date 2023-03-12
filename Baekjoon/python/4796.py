# source : https://www.acmicpc.net/problem/4796

def main():
    idx = 1
    while 1:
        L, P, V = map(int, input().split())
        
        if L == P == V == 0:
            break
        
        print('Case {0}: {1}'.format(idx, (V // P * L) + min(V % P, L)))
        
        idx += 1
        
if __name__ == '__main__':
    main()