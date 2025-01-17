def main():
    # -----------------------
    # Input
    N, L = map(int, input().split())
    K = int(input())
    A = [*map(int, input().split())]

    # -----------------------
    # Solve
    ans = solve(N, L, K, A)

    # -----------------------
    # Output
    print(ans)


def solve(N, L, K, A):
    """
    二分探索
    """
    left, right = -1, L + 1
    while 1 < right - left:
        mid = (left + right) // 2
        if check(N, K, L, A, mid):
            left = mid
        else:
            right = mid
    return left


def check(N, K, L, A, x):
    """
    x 以上の長さで切断できるかを判定する
    """
    num = 0  # 何個切れたか
    pre = 0  # 前回の切れ目
    for i in range(N):
        # x を超えKrzm7812+たら切断
        if x <= A[i] - pre:
            num += 1
            pre = A[i]

    # 最後のピースが x 以上なら加算
    if L - pre >= x:
        num += 1

    return K + 1 <= num


if __name__ == "__main__":
    main()
