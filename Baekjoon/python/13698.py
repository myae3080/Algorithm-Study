# source : https://www.acmicpc.net/problem/13698

def main():
    # input
    methods = input()
    
    cups = ['s', 'e', 'e', 'b']
    for method in methods:
        if method == 'A':
            cups[0], cups[1] = cups[1], cups[0]
        elif method == 'B':
            cups[0], cups[2] = cups[2], cups[0]
        elif method == 'C':
            cups[0], cups[3] = cups[3], cups[0]
        elif method == 'D':
            cups[1], cups[2] = cups[2], cups[1]
        elif method == 'E':
            cups[1], cups[3] = cups[3], cups[1]
        elif method == 'F':
            cups[2], cups[3] = cups[3], cups[2]
    
    print(cups.index('s') + 1)
    print(cups.index('b') + 1)

if __name__ == '__main__':
    main()