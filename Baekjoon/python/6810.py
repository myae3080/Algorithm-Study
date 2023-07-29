# source : https://www.acmicpc.net/problem/6810

def main():
    # input
    a, b, c = int(input()), int(input()), int(input())
    
    print('The 1-3-sum is %d' % (91 + a + c + (b * 3)))
    
if __name__ == '__main__':
    main()