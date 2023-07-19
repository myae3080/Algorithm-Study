# source : https://www.acmicpc.net/problem/1362

def main():
    index = 1
    while 1:
        # input
        o, w = map(int, input().split())
        
        if o == w == 0:
            break
        
        is_dead = False
        while 1:
            # input
            action, n = input().split()
            
            if action == '#':
                print(index, end=' ')
                print('RIP') if is_dead else print(':-)') if 2 * int(o) > w > int(o) // 2 else print(':-(')
                index += 1
                break
            
            if action == 'F':
                w += int(n)
            else:
                w -= int(n)
                if w <= 0:
                    is_dead = True

if __name__ == '__main__':
    main()