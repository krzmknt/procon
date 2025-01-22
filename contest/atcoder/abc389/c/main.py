def main():
    # -----------------------
    # Input
    [Q], *queries = [[*map(int, line.split())] for line in open(0)]

    snakes = []
    head_pos = []
    offset = 0
    offset_len = 0

    for q in queries:
        # Push
        if q[0] == 1:
            # print("Push", q[1])

            snake_len = q[1]

            if len(head_pos) == 0:
                head_pos.append(0)
            else:
                head_pos.append(head_pos[-1] + snakes[-1])

            snakes.append(snake_len)

        # Pop
        if q[0] == 2:
            # print("Pop")

            offset_len += snakes[offset]
            offset += 1

        # Query
        if q[0] == 3:
            # print("Query", q[1])
            pos = q[1]

            print(head_pos[pos - 1 + offset] - offset_len)

        # print("  snakes: ", snakes)
        # print("  head_pos: ", head_pos)
        # print("  offset: ", offset)
        # print("  offset_len: ", offset_len)


if __name__ == "__main__":
    main()
