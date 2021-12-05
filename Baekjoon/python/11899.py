# source : acmicpc.net/problem/11899
# data structure, string, stack

# input
s = input()

st = []
count = 0

for c in s:
    if c == "(":
        st.append(c)
    else:
        if len(st) == 0:
            count += 1
        else:
            st.pop()
            
print(count + len(st))