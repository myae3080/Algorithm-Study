# source : https://www.acmicpc.net/problem/6502

order = 1
while 1:
    # input
    info = list(map(int, input().split()))
    
    if len(info) == 1:
        break
    
    r, w, l = info
    diagonal = (w ** 2 + l ** 2) ** 0.5
    if 2 * r >= diagonal:
        print('Pizza {0} fits on the table.'.format(order))
    else:
        print('Pizza {0} does not fit on the table.'.format(order))
        
    order += 1