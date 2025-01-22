def main():
    # -----------------------
    # Input
    N, M = map(int, input().split())
    P = [*map(int, input().split())]
    P = sorted(P)

    ITEMS = []
    for p in P:
        for k in range(1, 10**100):
            if M < k**2 * p:
                break
            print(p, k**2 * p, k)
            ITEMS.append((k**2 * p, k))

    # dp[i] = max value when weight is i
    dp = [0] * (M + 1)

    for weight, value in ITEMS:
        dp = [*map(max, zip(dp, [0] * weight + [value + v for v in dp]))]

    print(dp[M])


def solve():
    return True


if __name__ == "__main__":
    main()
