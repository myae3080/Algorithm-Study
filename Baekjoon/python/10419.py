# source : https://www.acmicpc.net/problem/10419

def main():
    # input
    for _ in range(int(input())):
        # input
        d = int(input())
        
        tardy = 0
        while 1:
            if tardy + (tardy ** 2) > d:
                tardy -= 1
                break
            
            tardy += 1
        
        print(tardy)
    
if __name__ == '__main__':
    main()