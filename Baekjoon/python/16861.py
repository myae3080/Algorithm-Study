# source : https://www.acmicpc.net/problem/16861

def main():
    # input
    start_num = int(input())
    
    for num in range(start_num, 1000000001):
        digit_sum = sum([int(n) for n in str(num)])
        
        if num % digit_sum == 0:
            print(num)
            break

if __name__ == '__main__':
    main()