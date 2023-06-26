# source : https://www.acmicpc.net/problem/8949

def main():
    # input
    a, b = input().split()
    
    result = ''
    if a == b:
        for i in range(len(a)):
            result += str(int(a[i]) + int(b[i]))
    else:
        diff = abs(len(a) - len(b))
        
        if len(a) > len(b):
            b = '0' * diff + b
        else:
            a = '0' * diff + a
    
        for i in range(len(a)):
            result += str(int(a[i]) + int(b[i]))
        
    print(result)
    
if __name__ == '__main__':
    main()