n, r = map(int, input().split())

MOD = 10**9 + 7

modinv_table = [-1] * (r + 1)
modinv_table[1] = 1
for i in range(2, r + 1):
    modinv_table[i] = (-modinv_table[MOD % i] * (MOD // i)) % MOD


def binomial_coefficients(n, r):
    ans = 1
    for i in range(r):
        ans *= n - i
        ans *= modinv_table[i + 1]
        ans %= MOD

    return ans


print(binomial_coefficients(n, r))
