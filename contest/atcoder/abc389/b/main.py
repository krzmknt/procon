def main():
    # -----------------------
    # Input
    # 1
    X = int(input())
    # -----------------------
    # Solve

    fact = 1
    for n in range(2, 10000):
        fact *= n
        if X == fact:
            print(n)
            return


if __name__ == "__main__":
    main()
