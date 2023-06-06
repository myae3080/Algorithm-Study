# source : https://www.acmicpc.net/problem/4388

def main():
    while 1:
        # input
        a, b = input().split()
        
        if a == '0' and b == '0':
            break
        
        a_len, b_len = len(a), len(b)
        if a_len > b_len:
            b = (a_len - b_len) * '0' + b
        else:
            a = (b_len - a_len) * '0' + a
        
        result, carry = 0, 0
        for i in range(max(a_len, b_len) - 1, -1, -1):
            if int(a[i]) + int(b[i]) + carry > 9:
                result += 1
                carry = 1
            else:
                carry = 0
        
        print(result)

if __name__ == '__main__':
    main()