# source : https://www.acmicpc.net/problem/26069

def main():
    rainbow_dancing = {'ChongChong'}
    
    # input
    for _ in range(int(input())):
        # input
        a, b = input().split()
        
        if a in rainbow_dancing:
            rainbow_dancing.add(b)
        
        if b in rainbow_dancing:
            rainbow_dancing.add(a)

    print(len(rainbow_dancing))

if __name__ == '__main__':
    main()