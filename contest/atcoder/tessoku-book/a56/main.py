_, S, *QUERIES = open(0)


class HashedString:
    def __init__(self, S, base=100, mod=10**9 + 7):
        """
        S   : 対象の文字列
        base: 基数
        mod : ハッシュ値が肥大化しないように適当な素数を設定
        """

        self.base = base
        self.mod = mod

        self.__dp = [0]
        for char in S:
            self.__dp.append((self.__dp[-1] * self.base + ord(char)) % self.mod)

    def hash(self, l, r):
        """
        l文字目からr文字目までのハッシュ値を返す
        \sum_{i=1}^K B^{K-i} T[i]
        """

        return (
            self.__dp[r] - self.__dp[l - 1] * pow(self.base, r - l + 1, self.mod)
        ) % self.mod


h = HashedString(S)

for query in QUERIES:
    a, b, c, d = map(int, query.split())
    ans = h.hash(a, b) == h.hash(c, d)

    print(["No", "Yes"][ans])
