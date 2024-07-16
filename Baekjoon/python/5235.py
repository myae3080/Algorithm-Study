# source : https://www.acmicpc.net/problem/5235

def main():
    # input
    for _ in range(int(input())):
        odd_sum, even_sum = 0, 0
        
        # input
        for num in list(map(int, input().split()))[1:]:
            if num % 2 == 0:
                even_sum += num
            else:
                odd_sum += num
        
        if odd_sum > even_sum:
            print('ODD')
        elif odd_sum < even_sum:
            print('EVEN')
        else:
            print('TIE')

if __name__ == '__main__':
    main()