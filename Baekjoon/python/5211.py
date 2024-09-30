# source : https://www.acmicpc.net/problem/5211

def main():
    # input
    pitch = input().split('|')
    
    major_scale, minor_scale = ['C', 'F', 'G'], ['A', 'D', 'E']
    major, minor = 0, 0
    
    for p in pitch:
        if p[0] in major_scale:
            major += 1
        if p[0] in minor_scale:
            minor += 1
    
    if major == minor:
        if pitch[-1][-1] in major_scale:
            major += 1
        if pitch[-1][-1] in minor_scale:
            minor += 1
    
    print('C-major' if major > minor else 'A-minor')

if __name__ == '__main__':
    main()