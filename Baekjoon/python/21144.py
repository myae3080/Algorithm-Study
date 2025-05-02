# source : https://www.acmicpc.net/problem/21144

def main():
    # input
    n = int(input())
    integers = input()
    
    for i in range(1, n + 1):
        num = str(i)
        if num != integers[:len(num)]:
            print(num)
            
            break
        else:
            integers = integers[len(num):]

if __name__ == '__main__':
    main()