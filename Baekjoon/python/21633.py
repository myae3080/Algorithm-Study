# source : https://www.acmicpc.net/problem/21633

def main():
    # input
    k = int(input())
    
    commision = (k * 0.01) + 25
    
    if commision < 100:
        print(100)
    elif commision > 2000:
        print(2000)
    else:
        print(commision)

if __name__ == '__main__':
    main()