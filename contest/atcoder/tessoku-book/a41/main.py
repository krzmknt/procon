N, S = int(input()), input()

# 連続する3文字が同じかどうか
ans = any(S[i] == S[i + 1] == S[i + 2] for i in range(N - 2))

print(["No", "Yes"][ans])
