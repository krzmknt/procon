import bisect

_, *QUERIES = [[*map(int, line.split())] for line in open(0)]

S = []
listed_values = set()

for mode, value in QUERIES:
    # Query 1: Add value to set S
    if mode == 1:
        if not value in listed_values:
            bisect.insort_left(S, value)
            listed_values.add(value)
        continue

    # Query 2: Remove value from set S
    if mode == 2:
        if value in S:
            S.remove(value)
            listed_values.remove(value)
        continue

    # Query 3: Print minimum element in set S that is greater than or equal to
    #          the value
    pos = bisect.bisect_left(S, value)
    print(S[pos] if pos < len(S) else -1)
