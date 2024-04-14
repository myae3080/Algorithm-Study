# https://www.acmicpc.net/problem/17413

def main():
    # input
    s = input()
    
    result, temp = '', ''
    is_special = False
    for i in range(len(s)):
        if s[i] == '<':
            is_special = True
            
            if temp:
                result += temp[::-1]
                temp = ''
            
            result += s[i]
        elif s[i] == '>':
            is_special = False
            result += s[i]
        else:
            if is_special or s[i] == ' ':
                if temp:
                    result += temp[::-1]
                    temp = ''
                
                result += s[i]
            else:
                temp += s[i]
                
                if i == len(s) - 1:
                    result += temp[::-1]
        
    print(result)

if __name__ == '__main__':
    main()