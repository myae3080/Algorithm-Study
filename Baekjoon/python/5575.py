# source : https://www.acmicpc.net/problem/5575

for _ in range(3):
    # input
    sh, sm, ss, fh, fm, fs = map(int, input().split())
    
    time = (fh - sh) * 3600 + (fm - sm) * 60 + (fs - ss)
    
    print(time // 3600, (time % 3600) // 60,  (time % 3600) % 60)