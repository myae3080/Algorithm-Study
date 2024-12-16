# source : https://www.acmicpc.net/problem/25870

def main():
    # input
    line = input()
    
    chars_count = [0] * 26
    for c in line:
        chars_count[ord(c) - 97] += 1
    
    odd, even = 0, 0
    for cnt in chars_count:
        if cnt != 0:
            if cnt % 2 == 0:
                even += 1
            else:
                odd += 1
    
    if odd != 0 and even != 0:
        print(2)
    elif odd != 0:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()