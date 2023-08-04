# source : https://www.acmicpc.net/problem/6763

def main():
    # input
    over = int(input()) - int(input())
    
    if over >= 0:
        print('Congratulations, you are within the speed limit!')
    else:
        fine = ''
        if abs(over) <= 20:
            fine = '100'
        elif 21 <= abs(over) <= 30:
            fine = '270'
        else:
            fine = '500'
        
        print('You are speeding and your fine is ${0}.'.format(fine))

if __name__ == '__main__':
    main()