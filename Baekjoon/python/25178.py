# source : https://www.acmicpc.net/problem/25178

def main():
    # input
    N = int(input())
    origin, change = input(), input()
    
    if origin[0] != change[0] or origin[-1] != change[-1]:
        print('NO')
        return
    
    origin_alpha, change_alpha = [0] * 26, [0] * 26
    new_origin, new_change = '', ''
    for i in range(1, N - 1):
        origin_alpha[ord(origin[i]) - 97] += 1
        change_alpha[ord(change[i]) - 97] += 1
        
        if origin[i] not in ['a', 'e', 'i', 'o', 'u']:
            new_origin += origin[i]
            
        if change[i] not in ['a', 'e', 'i', 'o', 'u']:
            new_change += change[i]
    
    if origin_alpha != change_alpha:
        print('NO')
        return
    
    if new_origin != new_change:
        print('NO')
        return
    
    print('YES')

if __name__ == '__main__':
    main()