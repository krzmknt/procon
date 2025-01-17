(_, s), A = [[*map(int, line.split())] for line in open(0)]

S = {0}
for a in A:
    S |= {a + x for x in S}

print(["No", "Yes"][s in S])
