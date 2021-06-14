# math

# 너무 복잡 -> 더 쉽게 짜는 법 고려
while True:
    # input
    input_list = list(map(int, input().split()))

    page = input_list[0]

    if page == 0:
        break

    target = input_list[1]
    page_list = []

    if target % 2 == 0:
        temp = target - 1
        page_list.append(temp)

        if temp <= (page // 2):
            page_list.append(page - temp) 
            page_list.append(page - temp + 1)
        else:
            page_list.append(page - temp)
            page_list.append(page - temp + 1)
    else:
        temp = target + 1
        page_list.append(temp)

        if temp <= (page // 2):
            page_list.append(page - temp + 1) 
            page_list.append(page - temp + 2)
        else:
            page_list.append(page - temp + 1) 
            page_list.append(page - temp + 2)

    for i, num in enumerate(sorted(page_list)):
        if i == (len(page_list) - 1):
            print(num)
        else:
            print(num, end=' ')