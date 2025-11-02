# source : https://www.acmicpc.net/problem/34509

def main():
    answers = []
    for num in range(10, 100):
        digits = list(str(num))

        if int(''.join(digits[::-1])) % 4 != 0:
            continue
        
        if sum([int(n) for n in digits]) % 6 != 0:
            continue
        
        if '8' in digits:
            continue
        
        answers.append(num)

    print(answers[0])

if __name__ == '__main__':
    main()