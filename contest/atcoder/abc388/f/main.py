"""
ABC388
E - Dangerous Sugoroku
@marked 2 pointers
"""


def main():
    # -----------------------
    # Input
    (N, M, A, B), *C = [[*map(int, line.split())] for line in open(0)]
    # print(N, M, A, B, C)

    # -----------------------
    # Solve
    D = [0] * (N - 1) + [1]

    for l, r in C:
        for i in range(l - 1, r):
            D[i] = -1

    idx = N - 1
    while 0 <= idx:
        for i in range(A, B + 1):
            if 0 <= idx - i < N and D[idx - i] == 0:
                D[idx - i] = 1

        idx -= 1
        if not 0 <= idx < N:
            break
        while 0 <= idx < N and D[idx] != 1:
            idx -= 1

    ans = D[0] == 1
    # -----------------------
    # Output
    print(["No", "Yes"][ans])


if __name__ == "__main__":
    main()
