N = int(input())

ans = 0
MOD = 10000

for _ in range(N):
    t, a = input().split()

    if t == "+":
        ans = (ans + int(a)) % MOD

    elif t == "-":
        ans = (ans - int(a)) % MOD

    elif t == "*":
        ans = (ans * int(a)) % MOD

    print(ans)
