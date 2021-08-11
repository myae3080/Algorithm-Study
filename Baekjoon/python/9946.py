# source : https://www.acmicpc.net/problem/9946

case = 0

while True:
    # input
    a = input()
    b = input()

    if a == 'END' and b == 'END':
        break

    case += 1

    a_list = sorted([s for s in a])
    b_list = sorted([s for s in b])

    if a_list == b_list:
        print('Case {}: same'.format(case))
    else:
        print('Case {}: different'.format(case))