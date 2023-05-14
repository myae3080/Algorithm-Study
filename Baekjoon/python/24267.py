# source : 

def main():
    # input
    n = int(input())
    
    print(0) if n < 3 else print(int((n * (n - 1) * (n - 2)) / 6))
    print(3)
    
if __name__ == '__main__':
    main()