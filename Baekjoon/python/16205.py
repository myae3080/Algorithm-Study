# source : https://www.acmicpc.net/problem/16205

def main():
    # input
    num, case = input().split()
    
    if num == '1':
        snake = ''
        for c in case:
            if c.isupper():
                snake += '_' + c.lower()
            else:
                snake += c
        pascal = case[0].upper() + case[1:]
        
        print(case)
        print(snake)
        print(pascal)
    elif num == '2':
        camel = ''
        next_upper = False
        for c in case:
            if c == '_':
                next_upper = True
            else:
                if next_upper:
                    camel += c.upper()
                    next_upper = False
                else:
                    camel += c
        pascal = camel[0].upper() + camel[1:]

        print(camel)
        print(case)
        print(pascal)
    else:
        camel = case[0].lower() + case[1:]
        snake = ''
        for c in camel:
            if c.isupper():
                snake += '_' + c.lower()
            else:
                snake += c
        
        print(camel)
        print(snake)
        print(case)

if __name__ == '__main__':
    main()