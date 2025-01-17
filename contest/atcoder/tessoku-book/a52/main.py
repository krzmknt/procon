from collections import deque

queue = deque()

for _ in range(int(input())):
    query = input().split()

    if query[0] == "1":
        queue.append(query[1])

    elif query[0] == "2":
        print(queue[0])

    else:
        queue.popleft()
