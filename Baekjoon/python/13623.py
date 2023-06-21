# source : https://www.acmicpc.net/problem/13623

def main():
    # input
    zero_or_one = list(map(int, input().split()))
    
    people = {0: 'A', 1: 'B', 2: 'C'}
    
    if len(set(zero_or_one)) == 1:
        print('*')
    else:
        if zero_or_one.count(1) == 2:
            print(people.get(zero_or_one.index(0)))
        else:
            print(people.get(zero_or_one.index(1)))
            
if __name__ == '__main__':
    main()