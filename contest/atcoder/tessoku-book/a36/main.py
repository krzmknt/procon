n, k = map(int, input().split())

print(["No", "Yes"][(2 * (n - 1) <= k) and (k % 2 == 0)])
