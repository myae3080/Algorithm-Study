# math

# input
count = int(input())

for i in range(count):
    floor = int(input())
    room_number = int(input())
    people_num_list = []

    # base floor setting
    for j in range(0, room_number):
        people_num_list.append(j + 1)

    while floor:
        total = 1

        for num in range(room_number):
            if num != 0:
                total += people_num_list[num]
                people_num_list[num] = total
            else:
                people_num_list[num] = 1

        floor -= 1

    print(total)