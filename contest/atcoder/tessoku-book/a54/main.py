Q = int(input())
QUERIES = [input().split() for _ in range(Q)]

scores = {}

for mode, person, *score in QUERIES:
    # Query 1: Register the score
    if mode == "1":
        scores[person] = int(score[0])

    # Query 2: Get the score
    else:
        print(scores[person])
