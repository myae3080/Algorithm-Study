# data structure, string, stack

result_list = []

while True:
    input_string = input().rstrip()
    st = []

    # break
    if input_string == ".":
        break

    for ch in input_string:
        if ch == "(" or ch == "[":
            st.append(ch)
        elif ch == ")":
            if st and st[-1] == "(":
                st.pop()
            else:
                result_list.append("no")
                break
        elif ch == "]":
            if st and st[-1] == "[":
                st.pop()
            else:
                result_list.append("no")
                break
        else:
            if ch == ".":
                if st:
                    result_list.append("no")
                else:
                    result_list.append("yes")

[print(s) for s in result_list]