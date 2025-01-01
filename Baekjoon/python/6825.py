# source : https://www.acmicpc.net/problem/6825

def main():
    # input
    weight, height = float(input()), float(input())

    bmi = round(weight / (height * height), 1)

    if bmi > 25:
        print('Overweight')
    elif bmi > 18.5:
        print('Normal weight')
    else:
        print('Underweight')

if __name__ == '__main__':
    main()