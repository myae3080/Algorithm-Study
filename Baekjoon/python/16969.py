# source : https://www.acmicpc.net/problem/16969

def main():
    # input
    car_number = input()
    
    nums, chars = 10, 26
    result = 1
    for i in range(len(car_number)):
        if i == 0:
            result *= nums if car_number[i] == 'd' else chars
        else:
            if car_number[i - 1] == 'd':
                result *= (nums - 1) if car_number[i] == 'd' else chars
            else:
                result *= nums if car_number[i] == 'd' else (chars - 1)
                
        result %= 1000000009
        
    print(result)

if __name__ == '__main__':
    main()