# source : https://www.acmicpc.net/problem/3054

def main():
    # input
    alpha = input()

    for i in range(1, 6):
        frame = ''
        if i == 3:
            frame = '#'
        else:
            frame = '.'

        if i == 3:
            for j in range(1, len(alpha) + 1):
                frame += ('.' + alpha[j - 1])
                if j % 3 == 0:
                    frame += '.*'
                elif j % 3 == 2:
                    if j < len(alpha):
                        frame += '.*'
                    else:
                        frame += '.#'
                else:
                    frame += '.#'
        elif i % 2 == 0:
            for j in range(1, len(alpha) + 1):
                if j % 3 == 0:
                    frame += '*.*.'
                else:
                    frame += '#.#.'
        else:
            for j in range(1, len(alpha) + 1):
                if j % 3 == 0:
                    frame += '.*..'
                else:
                    frame += '.#..'
        
        print(frame)

if __name__ == '__main__':
    main()