import itertools

(_, k), A, B, C, D = [[*map(int, l.split())] for l in open(0)]


# ------------------------
# Binary Search
# ------------------------
def bin_search(arr, x) -> bool:
    n = len(arr)
    l = 0
    r = n - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == x:
            return True
        if arr[m] < x:
            l = m + 1
        else:
            r = m - 1
    return False


# ------------------------
# calc
# ------------------------
E = sorted(list({a + b for a, b in itertools.product(A, B)}))
F = sorted(list({c + d for c, d in itertools.product(C, D)}))

ans = False

for e in E:
    if k < e:
        break

    if bin_search(F, k - e):
        ans = True
        break

print(["No", "Yes"][ans])
