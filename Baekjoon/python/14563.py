# source : https://www.acmicpc.net/problem/14563

def main():
    # input
    n = int(input())
    nums = list(map(int, input().split()))
    
    for num in nums:
        result = getSumOfDivisors(num)
        
        if result == num:
            print('Perfect')
        elif result < num:
            print('Deficient')
        else:
            print('Abundant')
    
def getSumOfDivisors(n: int) -> int:
    sumNum = 0
    for i in range(1, n):
        if n % i == 0:
            sumNum += i
            
    return sumNum
    
if __name__ == '__main__':
    main()