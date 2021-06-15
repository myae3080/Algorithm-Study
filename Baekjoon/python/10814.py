# string, sorting

# input
[print(ele[0], ele[1]) for ele in sorted([input().split() for i in range(int(input()))], key = lambda li: int(li[0]))]