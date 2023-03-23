# source : https://www.acmicpc.net/problem/4690

def main():
    for a in range(2, 101):
        for b in range(2, 101):
            for c in range(b + 1, 101):
                for d in range(c + 1, 101):
                    if a ** 3 == b ** 3 + c ** 3 + d ** 3:
                        print('Cube = {0}, Triple = ({1},{2},{3})'.format(a, b, c, d))
                        
if __name__ == '__main__':
    main()