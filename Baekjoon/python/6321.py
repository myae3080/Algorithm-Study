# source : https://www.acmicpc.net/problem/6321

for i in range(int(input())):
    # input
    string = input()

    result = ''
    for s in string:
        ascii = ord(s) + 1

        if ascii > 90:
            result += chr(65)
        else:
            result += chr(ascii)

    print('String #' + str(i + 1))
    print(result)
    print()