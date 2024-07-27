# source : https://www.acmicpc.net/problem/21591

def main():
    # input
    laptop_w, laptop_h, sticker_w, sticker_h = map(int, input().split())

    if laptop_w >= (sticker_w + 2) and laptop_h >= (sticker_h + 2):
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()