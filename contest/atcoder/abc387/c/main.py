def main():
    # -----------------------
    # Input
    L, R = map(int, input().split())

    # -----------------------
    # Output
    print(solve(R) - solve(L - 1))


def solve(N):
    """N以下のヘビ数の数を返す"""
    ans = 0
    l = len(str(N))
    digits = [int(d) for d in str(N)]

    print(N, "について考える")

    # Nの桁数-1 までは全量合計する
    for d in digits:
        ans += num_snake(d)

    # N の桁数の場合は戦闘の数字に制約を課して計算する
    for n in range(1, digits[0]):
        ans += num_snake2(n, digits[0])

    # left_most_difit から始まる num_digit 桁のヘビ数の数を求める
    for d in digits[1:]:
        if d == 0:
            continue
        ans += min(d, digits[0]) * (digits[0] ** (digits[0] - d - 1))

    ans += min(digits[-1] + 1, digits[0])
    print(N, "以下のヘビ数の数は", ans)
    return ans


def num_snake(d):
    "d桁ヘビ数の数を求める"
    ans = 1
    for n in range(2, 10):
        ans += num_snake2(n, d)
    print(d, "桁ヘビ数の数は", ans)
    return ans


def num_snake2(n, d):
    "nから始まるd桁ヘビ数の数を求める"
    print(n, "から始まる", d, "桁のヘビ数の数は", n ** (d - 1))
    return n ** (d - 1)


if __name__ == "__main__":
    main()
