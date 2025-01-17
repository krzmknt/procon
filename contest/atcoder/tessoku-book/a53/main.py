import heapq

[Q], *QUERIES = [[*map(int, line.split())] for line in open(0)]

min_heap = []
heapq.heapify(min_heap)


for query in QUERIES:
    # 1 : Insert x in the heap.
    if query[0] == 1:
        heapq.heappush(min_heap, query[1])

    # 2 : Print the minimum of all the elements in the heap.
    elif query[0] == 2:
        min = heapq.heappop(min_heap)
        print(min)
        heapq.heappush(min_heap, min)

    # 3: Delete the minimum of all the elements in the heap.
    else:
        heapq.heappop(min_heap)
