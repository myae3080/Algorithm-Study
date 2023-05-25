# source : https://www.acmicpc.net/problem/28113

def main():
    # input
    n, bus, subway = map(int, input().split())
    
    if bus == subway:
        print('Anything')
    elif bus < subway:
        print('Bus')
    else:
        print('Subway')
        
if __name__ == '__main__':
    main()