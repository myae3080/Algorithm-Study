# source : https://www.acmicpc.net/problem/6779

def main():
    # input
    h, M = int(input()), int(input())
    
    time = 1
    while time <= M:
        A = (-6 * (time ** 4)) + (h * (time ** 3)) + (2 * (time ** 2)) + time
        
        if A <= 0:
            print('The balloon first touches ground at hour: %d' % time)
            return
        
        time += 1
    
    print('The balloon does not touch ground in the given time.')

if __name__ == '__main__':
    main()