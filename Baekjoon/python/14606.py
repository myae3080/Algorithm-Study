# source : https://www.acmicpc.net/problem/14606

def main():
    # input
    n = int(input())
    
    if n == 1:
        print(0)
        return
    
    heights = [n]
    happy = 0
    while heights.count(1) < n:
        for height in heights:
            if height > 1:
                a = height // 2
                b = height - a
                
                happy += a * b
                heights.append(a)
                heights.append(b)

    print(happy)

if __name__ == '__main__':
    main()