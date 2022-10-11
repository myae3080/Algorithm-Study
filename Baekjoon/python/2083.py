# source : https://www.acmicpc.net/problem/2083

while 1:
    # input
    name, age, weight = input().split()
    
    if name == '#':
        break

    if int(age) > 17 or int(weight) >= 80:
        print(name, 'Senior')
    else:
        print(name, 'Junior')