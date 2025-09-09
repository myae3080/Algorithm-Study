# source : https://www.acmicpc.net/problem/14626

def main():
    # input
    isbn = input()

    s = 0
    weight = 1
    for i in range(len(isbn)):
        if isbn[i] == '*':
            if i % 2 == 1:
                weight = 3
            
            continue

        if i % 2 == 0:
            s += int(isbn[i])
        else:
            s += int(isbn[i]) * 3
    
    for i in range(10):
        if (i * weight + s) % 10 == 0:
            print(i)

            break

if __name__ == '__main__':
    main()