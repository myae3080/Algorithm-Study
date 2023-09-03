# source : https://www.acmicpc.net/problem/10173

def main():
    while 1:
        # input
        sentence = input()

        if sentence == 'EOI':
            break

        print('Found' if sentence.lower().count('nemo') > 0 else 'Missing')
    
if __name__ == '__main__':
    main()