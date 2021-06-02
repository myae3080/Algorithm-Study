# math

# input
room_num = int(input())

total_room_num = 1
room_count = 1

while room_num > total_room_num:
    total_room_num += 6 * room_count
    room_count += 1

print(room_count)