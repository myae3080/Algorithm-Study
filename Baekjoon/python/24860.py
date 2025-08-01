# source : https://www.acmicpc.net/problem/24860

def main():
    # input
    Vk, Jk = map(int, input().split())
    Vl, Jl = map(int, input().split())
    Vh, Dh, Jh = map(int, input().split())

    print(((Vk * Jk) + (Vl * Jl)) * (Vh * Dh * Jh))

if __name__ == '__main__':
    main()