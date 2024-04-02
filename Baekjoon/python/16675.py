# source : https://www.acmicpc.net/problem/16675

def main():
    # input
    ml, mr, tl, tr = input().split()
        
    if ml != mr and tl != tr:
        print('?')
    elif ml == mr and tl != tr:
        if ml == 'R' and (tl == 'P' or tr == 'P'):
            print('TK')
        elif ml == 'S' and (tl == 'R' or tr == 'R'):
            print('TK')
        elif ml == 'P' and (tl == 'S' or tr == 'S'):
            print('TK')
        else:
            print('?')
    elif ml != mr and tl == tr:
        if tl == 'R' and (ml == 'P' or mr == 'P'):
            print('MS')
        elif tl == 'S' and (ml == 'R' or mr == 'R'):
            print('MS')
        elif tl == 'P' and (ml == 'S' or mr == 'S'):
            print('MS')
        else:
            print('?')
    else:
        if ml == 'R':
            print('?') if tl == 'R' else print('MS') if tl == 'S' else print('TK')
        elif ml == 'S':
            print('TK') if tl == 'R' else print('?') if tl == 'S' else print('MS')
        else:
            print('MS') if tl == 'R' else print('TK') if tl == 'S' else print('?')
    
if __name__ == '__main__':
    main()