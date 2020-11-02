from itertools import permutations

perm = permutations(['A','A','A','A','A','A','A','A','C','C','C','C','C','C','C','C','G','G','G','G','G','G','G','G','T','T','T','T','T','T','T','T'],8)

mers = []

for i in perm:
    mers.append(','.join(i))

print(mers)