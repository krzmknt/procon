(N), A = [[*map(int, line.split())] for line in open(0)]

# 増大したら記録せず、減少したら記録して減少列を作る

arr = [(1, A[0])]
ans = [-1]
for i, val in enumerate(A[1:]):
    i += 2
    prev_i, prev_val = arr[-1]
    if prev_val > val:
        ans.append(prev_i)
        arr.append((i, val))
    else:
        # それより大きい値が見つかるまでポップして、その後に追加
        while arr and arr[-1][1] < val:
            arr.pop()

        if not arr:
            ans.append(-1)
        else:
            ans.append(arr[-1][0])
        arr.append((i, val))

print(*ans)
