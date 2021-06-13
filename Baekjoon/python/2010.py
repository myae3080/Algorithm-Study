# math

import sys

# input
multitap_count = int(input())
plug_list = [int(sys.stdin.readline()) for i in range(multitap_count)]

com_count = 0

for i, plug in enumerate(plug_list):
    if i != len(plug_list) - 1:
        com_count += plug - 1
    else:
        com_count += plug

print(com_count)