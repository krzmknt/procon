(_, MAX_WEIGHT), *ITEMS = [map(int, line.split()) for line in open(0)]

# dp[i] = max value when weight is i
dp = [0] * (MAX_WEIGHT + 1)

for weight, value in ITEMS:
    dp = [*map(max, zip(dp, [0] * weight + [value + v for v in dp]))]

print(dp[MAX_WEIGHT])
