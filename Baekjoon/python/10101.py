# input
angle_list = [int(input()) for n in range(3)]

if sum(angle_list) != 180:
    print('Error')
else:
    angle_count = len(set(angle_list))

    if angle_count == 1:
        print('Equilateral')
    elif angle_count == 2:
        print('Isosceles')
    else:
        print('Scalene')