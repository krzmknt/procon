N, L = map(int, input().split())

ans = 0
for _ in range(N):
    a, d = input().split()
    a = int(a)
    if d == 'E':
        ans = max(ans, L-a)
    else:
        ans = max(ans, a)
print(ans)
