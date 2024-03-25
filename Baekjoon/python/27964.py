# source : https://www.acmicpc.net/problem/27964

def main():
    # input
    n = input()
    toppings = input().split()

    cheese = []
    for topping in toppings:
        if topping.endswith('Cheese') and topping not in cheese:
            cheese.append(topping)

    print('yummy' if len(cheese) >= 4 else 'sad')

if __name__ == '__main__':
    main()