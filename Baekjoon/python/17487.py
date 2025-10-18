# source : https://www.acmicpc.net/problem/17487

def main():
    rights = ['u', 'h', 'n', 'i', 'j', 'm', 'o', 'k', 'p', 'l']

    # input
    s = input()

    left, right = 0, 0
    for c in s:
        if c == ' ':
            if right < left:
                right += 1
            else:
                left += 1

            continue

        char = c.lower()
        if char in rights:
            right += 1
        else:
            left += 1

        if c.isupper():
            if right < left:
                right += 1
            else:
                left += 1
        
    print(left, right)

if __name__ == '__main__':
    main()