# source : https://www.acmicpc.net/problem/20540
# string

dict = {"E":"I", "S":"N", "T":"F", "J":"P", "I":"E", "N":"S", "F":"T", "P":"J"}

[print(dict[s], end='') for s in list(input())]