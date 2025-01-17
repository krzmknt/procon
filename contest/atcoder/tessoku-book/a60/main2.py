N = int(input())
A = [*map(int, input().split())]

stack = []
ans = []

for index, val in enumerate(A):
    # 空になるか、自分よりも大きい値が現れるまでポップする
    while 0 < len(stack) and stack[-1]["val"] <= val:
        stack.pop()
    ans.append(-1 if len(stack) == 0 else stack[-1]["id"])
    stack.append({"id": index + 1, "val": val})

print(*ans)
