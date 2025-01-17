(N, Q), A, *QUERIES = [[*map(int, line.split())] for line in open(0)]

jump = [[0, *A]]

# jump[i][j] := 位置 j の   2^i 日後の位置
#
#   [0, 1, ..., N] は 0 日目の位置
#   jump[0] = [A  [0], A  [1], ..., A  [N]] は 2^0 = 1 日目の位置
#   jump[1] = [A^2[0], A^2[1], ..., A^2[N]] は 2^1 = 2 日目の位置
#   jump[2] = [A^4[0], A^4[1], ..., A^4[N]] は 2^2 = 4 日目の位置
#   ...
#   jump[i] は 2^i 日目の位置

# 29 回 doubling すると最大を超える (Y <= 10^9 < 2^30)
for _ in range(29):
    B = jump[-1]
    jump.append([B[B[pos]] for pos in range(N + 1)])

for pos, days in QUERIES:
    # e.g., 13 = 1101(2) -reverse-> 1 0 1 1
    #                          exp: 0 1 2 3
    #                          => 2^0, 2^2, 2^3 日の移動を行う
    for exp, bit in enumerate(reversed(format(days, "b"))):
        if bit == "1":
            pos = jump[exp][pos]

    print(pos)


