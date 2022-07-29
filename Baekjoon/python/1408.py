# source : https://www.acmicpc.net/problem/1408

# input
start, now = input().split(':'), input().split(':')

start_sec = (int(start[0]) * 3600) + (int(start[1]) * 60) + int(start[2])
now_sec = (int(now[0]) * 3600) + (int(now[1]) * 60) + int(now[2])
remain_sec = now_sec - start_sec

if remain_sec < 0: 
    remain_sec += 3600 * 24

h = remain_sec // 3600
remain_sec %= 3600
m = remain_sec // 60
remain_sec %= 60
s = remain_sec

print(str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2))