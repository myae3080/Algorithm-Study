# source : https://www.acmicpc.net/problem/4583

def main():
    mirror_char = ['b', 'd', 'i', 'o', 'p', 'q', 'v', 'w', 'x']

    while 1:
        # input
        word = input()

        if word == '#':
            break

        is_valid = True
        result = ''
        for c in word[::-1]:
            if c not in mirror_char:
                is_valid = False
                break
            else:
                if c == 'b':
                    result += 'd'
                elif c == 'd':
                    result += 'b'
                elif c == 'p':
                    result += 'q'
                elif c == 'q':
                    result += 'p'
                else:
                    result += c

        print(result if is_valid else 'INVALID')

if __name__ == '__main__':
    main()