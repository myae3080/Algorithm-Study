# source : 

def main():
    fruits = {}

    # input
    n = int(input())

    for _ in range(n):
        # input
        fruit, cnt = input().split()

        if fruit in fruits:
            fruits[fruit] += int(cnt)
        else:
            fruits[fruit] = int(cnt)
    
    print('YES' if 5 in fruits.values() else 'NO')

if __name__ == '__main__':
    main()