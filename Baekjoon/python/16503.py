# source : https://www.acmicpc.net/problem/16503

def main():
    # input
    k1, o1, k2, o2, k3 = input().split()
    
    a1 = calculator(calculator(int(k1), int(k2), o1), int(k3), o2)
    a2 = calculator(int(k1), calculator(int(k2), int(k3), o2), o1)
    
    print(min(a1, a2))
    print(max(a1, a2))

def calculator(num1: int, num2: int, o: str) -> int:
    if o == '+':
        return num1 + num2
    elif o == '-':
        return num1 - num2
    elif o == '*':
        return num1 * num2
    elif o == '/':
        return int(num1 / num2)

if __name__ == '__main__':
    main()