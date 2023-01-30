# source : https://www.acmicpc.net/problem/9366

def main():
    # input
    for i in range(int(input())):
        # input
        sides = sorted(list(map(int, input().split())))
        
        type = ''
        if sides[-1] >= sum(sides[:2]):
            type = 'invalid!'
        else: 
            count = len(set(sides))
            if count == 1:
                type = 'equilateral'
            elif count == 2:
                type = 'isosceles'
            else:
                type = 'scalene'
            
        print('Case #{0}: {1}'.format(i + 1, type))

if __name__ == '__main__':
    main()