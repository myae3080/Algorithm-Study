# source : https://www.acmicpc.net/problem/1672

# input
n = int(input())
dna = list(input())

translations = {'AG': 'C', 'AC': 'A', 'AT': 'G', 'CG': 'T', 'GT': 'A', 'CT': 'G'}

while len(dna) > 1:
    bases = set([dna.pop(), dna.pop()])
    base = ''.join(sorted(bases))
    
    if base not in translations:
        dna.append(base)
    else:
        dna.append(translations[base])

print(dna[0])