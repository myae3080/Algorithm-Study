# source : https://www.acmicpc.net/problem/30402

def main():
    # input
    pixels = [list(input().split()) for _ in range(15)]
    
    for pixel in pixels:
        if 'w' in pixel:
            print('chunbae')
            break
        if 'b' in pixel:
            print('nabi')
            break
        if 'g' in pixel:
            print('yeongcheol')
            break

if __name__ == '__main__':
    main()