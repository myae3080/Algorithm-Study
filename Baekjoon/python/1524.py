# source : https://www.acmicpc.net/problem/1524

def main():
    # input
    for _ in range(int(input())):
        # input
        input()
        n, m = map(int, input().split())
        sj, sb = sorted(list(map(int, input().split())), reverse=True), sorted(list(map(int, input().split())), reverse=True)
        
        while sj and sb:
            if sj[-1] >= sb[-1]:
                sb.pop()
            else:
                sj.pop()
                
        if not sj and not sb:
            print('C')
        elif not sj:
            print('B')
        else:
            print('S')

if __name__ == '__main__':
    main()