# source : https://www.acmicpc.net/problem/26336

def main():
    # input
    for _ in range(int(input())):
        # input
        total, gas, food = map(int, input().split())
        
        miles = [0] * (total + 1)
        interval1 = gas
        while interval1 < total:
            miles[interval1] = 1
            interval1 += gas
        
        interval2 = food
        while interval2 < total:
            miles[interval2] = 1
            interval2 += food
        
        print(total, gas, food)
        print(miles.count(1))

if __name__ == '__main__':
    main()