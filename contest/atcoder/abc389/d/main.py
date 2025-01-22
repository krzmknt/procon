def main():
    # -----------------------
    # Input
    R = int(input())

    ans = 0
    # -----------------------
    # Solve

    for x in range(-R + 1, R):
        x0 = x - 0.5
        if 0 < x:
            x0 += 1

        y = int((R**2 - x0**2) ** 0.5 - 0.5)

        ans += y * 2 + 1

    # -----------------------
    # Output
    print(ans)


def solve():
    return True


if __name__ == "__main__":
    main()
