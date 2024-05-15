# source : https://www.acmicpc.net/problem/4597

def main():
    while 1:
        # input
        bit_string = input()
        
        if bit_string == '#':
            break
        
        if bit_string[-1] == 'o':
            print(bit_string.replace('o', '0') if bit_string.count('1') % 2 == 1 else bit_string.replace('o', '1'))
        else:
            print(bit_string.replace('e', '1') if bit_string.count('1') % 2 == 1 else bit_string.replace('e', '0'))

if __name__ == '__main__':
    main()