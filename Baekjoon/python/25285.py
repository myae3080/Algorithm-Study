# source : https://www.acmicpc.net/problem/25285

def main():
    # input
    for _ in range(int(input())):
        # input
        height, weight = map(int, input().split())
        
        bmi = weight / ((height / 100) ** 2)
        
        if height < 140.1:
            print(6)
        elif 140.1 <= height < 146:
            print(5)
        elif 146 <= height < 159:
            print(4)
        elif 159 <= height < 161:
            if 16 <= bmi < 35:
                print(3)
            else:
                print(4)
        elif 161 <= height < 204:
            if 20 <= bmi < 25:
                print(1)
            elif 18.5 <= bmi < 20 or 25 <= bmi < 30:
                print(2)
            elif 16 <= bmi < 18.5 or 30 <= bmi < 35:
                print(3)
            else:
                print(4)
        else:
            print(4)
            
if __name__ == '__main__':
    main()