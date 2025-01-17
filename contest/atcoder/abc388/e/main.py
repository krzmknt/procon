def main():
    # -----------------------
    # Input
    N = int(input())
    A = [*map(int, input().split())]

    # -----------------------
    # Solve
    ans = 0

    l = 0
    r = N // 2

    while l < N // 2 and r < N:
        if 2 * A[l] <= A[r]:
            ans += 1
            l += 1
            r += 1
        else:
            r += 1

    # -----------------------
    # Output
    print(ans)


if __name__ == "__main__":
    main()
