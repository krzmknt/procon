def main():
    # -----------------------
    # Input
    X = int(input())

    # -----------------------
    # Solve
    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if not i * j == X:
                ans += i * j

    # -----------------------
    # Output
    print(ans)


if __name__ == "__main__":
    main()
