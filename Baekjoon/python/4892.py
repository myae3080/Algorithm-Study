# source : https://www.acmicpc.net/problem/4892

order = 1
while 1:
    # input
    n = int(input())
    
    if n == 0:
        break
    
    n1 = 3 * n
    if n1 % 2 == 0:
        n2 = n1 // 2
    else:
        n2 = (n1 + 1) // 2
        
    n3 = 3 * n2
    n4 = n3 // 9
    if n1 % 2 == 0:
        print('{0}. {1} {2}'.format(int(order), 'even', int(n4)))
    else:
        print('{0}. {1} {2}'.format(int(order), 'odd', int(n4)))
    
    order += 1