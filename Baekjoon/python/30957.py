# source : https://www.acmicpc.net/problem/30957

def main():
    # input
    n = int(input())
    fields = input()
    
    b, s, a = fields.count('B'), fields.count('S'), fields.count('A')
    
    if b == s == a:
        print('SCU')
    else:
        result = ''
        
        if b == max(b, s, a):
            result += 'B'
        if s == max(b, s, a):
            result += 'S'
        if a == max(b, s, a):
            result += 'A'
        
        print(result)

if __name__ == '__main__':
    main()