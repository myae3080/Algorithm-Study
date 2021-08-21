# source : https://www.acmicpc.net/problem/2857
# string

fbi_list = []

for i in range(5):
    # input
    if 'FBI' in input():
        fbi_list.append(str(i + 1))

if len(fbi_list) > 0:
    print(' '.join(fbi_list))
else:
    print('HE GOT AWAY!')