def is_substring(S: str, T: str):
    """
    Check if S is substring of T

    Parameters:
    S: str
    T: str

    Returns:
    bool: True if S is substring of T, False otherwise

    Examples:
    is_substring('123', "___1__2__3") -> True

    Complexity: O(len(T))
    """
    if len(S) == 0 and 0 <= len(T):
        return True

    s_index = 0
    for t_index in range(len(T)):
        if S[s_index] == T[t_index]:
            s_index += 1
            if s_index == len(S):
                return True
    return False


def manacher(S):
    """
    Logest Palindromic Substring (Manacher's Algorithm)
    偶数長含めた回文の長さを求める
    radius[2*i] = L: S[i]を中心とする奇数長の最大回文
    radius[2*i+1] = L: S[i:i+2]を中心とする偶数長の最大回文
    ダミー文字を挟むが、各 radius[i] は実際の回文の文字列長と一致する

    Parameters:
    string: string

    Returns:
    list[int]: radius

    Examples:
    manacher("toyota") -> [0, 1, 0, 1, 0, 1, 0, 3, 0, 1, 0, 1, 0]

    Complexity: O(len(S))

    k = n - j
                <   i     >
    index | 0 1 2 3 4 5 6 7 8 9
    value | a # b # c # b # a #
          |
    j = 0 | [                 ]
    j = 1 |  [               ]
    j = 2 |   [             ]
    j = 3 |    [           ]
    j = 4 |     [         ]
    j = 5 |      [       ]
    j = 6 |       [     ]
    j = 7 |        [   ]
    j = 8 |         [ ]



    """

    # "abc" -> "a#b#c"
    C = "#".join(list(S))

    L = len(C)

    radius = [0] * L

    def a(i, j):
        return j <= i < L - j and C[i - j] == C[i + j]

    i = j = 0
    while i < L:
        while j <= i < L - j and C[i - j] == C[i + j]:
            j += 1

        radius[i] = j
        k = 1
        while j - radius[i - k] > k <= i < L - k:
            radius[i + k] = radius[i - k]
            k += 1

        i += k
        j -= k

    for i in range(L):
        if i & 1 == radius[i] & 1:
            radius[i] -= 1

    return radius
