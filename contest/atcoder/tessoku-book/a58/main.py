from typing import Callable, Final, TypeVar


class SegmentTree:
    """
    Efficient data structure for range queries and updates.
    """

    T = TypeVar("T")

    def __init__(
        self, initial_list: list[T], evaluate: Callable[[T, T], T], identity: T | None = None
    ):
        """
        Complexity: O(N)

        Parameters:
        initial_list : 配列の初期値
        evalualte    : 更新、クエリに使う関数
        identity     : 単位元

        Examples:
        >>> seg = SegmentTree(initial_list=[1, 2, 3], eval=max, identity=0)
        seg.__tree_width = 4
        seg.tree = [-, 3, 2, 3, 1, 2, 3, 0] (1-indexed)
                                ^  ^  ^     (initial_lsits)
                 1:          a        b  c
                 2:       a     b  c
                 3:    a  b  c

        上記の順に a = max(b, c) を計算してセグメントツリーを構築する。
        ツリーとして見やすくするためにインデントすると次のようになる。

        seg.__tree = [-,
                   3,
             2,    3,
          1, 2, 3, 0, (<- Filled with initial_list)
        ]
        """

        # Calculate implicit identity
        if not identity:
            identity = initial_list[0]
            for element in initial_list:
                identity = evaluate(identity, element)

        # Number of leaves (the smallest power of 2 that is greater than or equal to N)
        self.__tree_width: Final = 1 << (len(initial_list) - 1).bit_length()

        self.__evaluate: Final = evaluate

        # Initialize the tree with identity and initial_list
        self.__tree = [identity] * 2 * self.__tree_width
        self.__tree[self.__tree_width : self.__tree_width + len(initial_list)] = initial_list

        # Construct Segment Tree from bottom to top
        for parent_pos in reversed(range(self.__tree_width)):
            left_child = self.__tree[2 * parent_pos]
            right_child = self.__tree[2 * parent_pos + 1]
            self.__tree[parent_pos] = self.__evaluate(left_child, right_child)

    def update(self, pos_to_be_updated: int, new_value):
        """
        Update the value at pos_to_be_updated to new_value

        Complexity: O(log N)

        Parameters:
        pos_to_be_updated : 更新する要素のインデックス (0-indexed)
        new_value         : 更新後の値
        """

        # Update the leaf
        pos = self.__tree_width + pos_to_be_updated
        self.__tree[pos] = new_value

        # Climbing up the tree (pos == 1 means root)
        while 1 < pos:
            parent_pos = pos >> 1
            sibling_pos = pos ^ 1
            self.__tree[parent_pos] = self.__evaluate(self.__tree[pos], self.__tree[sibling_pos])
            pos = parent_pos

    def query(self, l_pos: int, r_pos: int):
        """
        Return the result of eval function in [l_pos, r_pos).
        Note that l_pos is inclusive, r_pos is exclusive.

        Complexity: O(log N)

        Parameters:
        l_pos : Leftmost index of the query (0-indexed, inclusive)
        r_pos : Rightmost index of the query (0-indexed, exclusive)

        Examples:
        For enumerate(seg.__tree) = [(0, -),
                                  (1, 8),
                  (2, 4),         (3, 8),
          (4, 4), (5, 2), (6, 8), (7, 1),  # (0, 1, 2, 3 : original array index)
        ],

        >>> seg.query(0, 2)
        (0, 2) -> (4, 6) -> ()
        4
        """

        l_pos += self.__tree_width
        r_pos += self.__tree_width

        def right_child(pos: int) -> bool:
            return pos & 1 == 1  # odd

        result = self.__tree[l_pos]
        while l_pos < r_pos:
            if right_child(l_pos):
                result = self.__evaluate(result, self.__tree[l_pos])

                # Go to right cousin
                l_pos += 1

            if right_child(r_pos):
                result = self.__evaluate(result, self.__tree[r_pos - 1])

            # Go to parent
            l_pos >>= 1
            r_pos >>= 1

        return result


if __name__ == "__main__":
    (N, _), *QUERIES = [[*map(int, line.split())] for line in open(0)]

    seg = SegmentTree(initial_list=[0] * N, evaluate=max)

    for mode, a, b in QUERIES:
        # mode 1: update
        if mode == 1:
            seg.update(pos_to_be_updated=a - 1, new_value=b)

        # mode 2: get max value
        else:
            print(seg.query(l_pos=a - 1, r_pos=b - 1))
