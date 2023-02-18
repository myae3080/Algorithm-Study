# source : https://www.acmicpc.net/problem/2966

def main():
    # input
    n = int(input())
    answers = input()
    
    # 상근, 창영, 현진
    s, c, h = 0, 0, 0
    for i in range(n):
        # 상근
        if i % 3 == 0:
            if answers[i] == 'A':
                s += 1
        elif i % 3 == 1:
            if answers[i] == 'B':
                s += 1
        else:
            if answers[i] == 'C':
                s += 1
                
        # 창영
        if i % 4 == 0 or i % 4 == 2:
            if answers[i] == 'B':
                c += 1
        elif i % 4 == 1:
            if answers[i] == 'A':
                c += 1
        else:
            if answers[i] == 'C':
                c += 1
        
        # 현진
        if i % 6 < 2:
            if answers[i] == 'C':
                h += 1
        elif 1 < i % 6 < 4:
            if answers[i] == 'A':
                h += 1
        else:
            if answers[i] == 'B':
                h += 1
        
    max_value = max(s, c, h)
    print(max_value)
    if max_value == s:
        print('Adrian')
    if max_value == c:
        print('Bruno')
    if max_value == h:
        print('Goran')
    
if __name__ == '__main__':
    main()