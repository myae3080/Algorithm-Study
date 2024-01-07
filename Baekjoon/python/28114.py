# source : https://www.acmicpc.net/problem/28114

def main():
    members = []
    
    # input
    members.append((input().split()))
    members.append((input().split()))
    members.append((input().split()))

    years = sorted([int(member[1]) % 100 for member in members])
    members.sort(key=lambda member: -int(member[0]))
    
    print(''.join([str(year).zfill(2) for year in years]))
    print(''.join([member[2][0] for member in members]))

if __name__ == '__main__':
    main()