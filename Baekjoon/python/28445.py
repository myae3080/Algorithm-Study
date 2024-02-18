# source : https://www.acmicpc.net/problem/28445

def main():
    # input
    f_colors, m_colors = list(input().split()), list(input().split())
    
    f_colors.extend(m_colors)
    colors = sorted(set(f_colors))
    
    for b in colors:
        for t in colors:
            print(b, t)

if __name__ == '__main__':
    main()