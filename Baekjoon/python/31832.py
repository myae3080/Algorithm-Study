# source : https://www.acmicpc.net/problem/31832

def main():
    result = ''
    
    # input
    for _ in range(int(input())):
        # input
        s = input()
        
        if s.isdigit():
            continue
        
        if len(s) > 10:
            continue
        
        lower_cnt, upper_cnt = 0, 0
        for c in s:
            if c.isupper():
                upper_cnt += 1
            if c.islower():
                lower_cnt += 1
        
        if upper_cnt > lower_cnt:
            continue
        
        result = s
    
    print(result)

if __name__ == '__main__':
    main()