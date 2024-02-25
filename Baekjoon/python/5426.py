# source : https://www.acmicpc.net/problem/5426

def main():
    # input
    for _ in range(int(input())):
        # input
        letter = input()
        
        size = int(len(letter) ** 0.5)
        words = [''] * size
        for i in range(len(letter)):
            words[i % size] += letter[i]

        print(''.join(words[::-1]))

if __name__ == '__main__':
    main()