# math, binary search

input_num = int(input())
start = 1
end = input_num

# sqrt를 이용할 시 overflow 발생
while True:
    mid = (start + end) // 2
    square = mid ** 2

    if square == input_num:
        print(mid)
        break
    elif square < input_num:
        start = mid + 1
    elif square > input_num:
        end = mid - 1