# source : https://www.acmicpc.net/problem/28062

def main():
    # input
    n = int(input())
    candies = list(map(int, input().split()))
    
    result = 0
    odd_candies = []
    for candy in candies:
        if candy % 2 == 0:
            result += candy
        else:
            odd_candies.append(candy)
    
    if odd_candies:
        if len(odd_candies) % 2 == 0:
            result += sum(odd_candies)
        else:
            odd_candies.sort()
            del odd_candies[0]
            result += sum(odd_candies)
    
    print(result)
    
if __name__ == '__main__':
    main()