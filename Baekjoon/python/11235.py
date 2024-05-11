# source : https://www.acmicpc.net/problem/11235

def main():
    vote_by_candidates = {}

    # input
    for _ in range(int(input())):
        # input
        candidate = input()

        if candidate not in vote_by_candidates:
            vote_by_candidates[candidate] = 1
        else:
            vote_by_candidates[candidate] += 1

    max_val = max(vote_by_candidates.values())
    for tu in sorted(vote_by_candidates.items(), key= lambda pair: (-pair[1], pair[0])):
        if tu[1] == max_val:
            print(tu[0])
        else:
            break

if __name__ == '__main__':
    main()