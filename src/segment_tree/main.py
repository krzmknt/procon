from typing import Callable, Final, TypeVar


class Node:
    def __init__(self, pos: int) -> None:
        self.pos = pos

    def parent_pos(self) -> int:
        return self.pos >> 1

    def left_child_pos(self) -> int:
        return self.pos << 1

    def right_child_pos(self) -> int:
        return self.pos << 1 | 1

    def is_left_child(self) -> bool:
        # even
        return self.pos & 1 == 0

    def is_right_child(self) -> bool:
        # odd
        return self.pos & 1 == 1


class SegmentTree:
    """
    Efficient data structure for range queries and updates.
    """

    T = TypeVar("T")

    def __init__(
        self,
        initial_list: list[T],
        evaluate: Callable[[T, T], T],
        identity: T,
    ) -> None:
        """
        Complexity: O(N)

        Parameters:
        initial_list : 配列の初期値
        evalualte    : 更新、クエリに使う関数
        identity     : 単位元

        Examples:
        >>> seg = SegmentTree(initial_list=[1, 2, 3], eval=max, identity=0)
        seg._tree_width = 4
        seg.tree = [-, 3, 2, 3, 1, 2, 3, 0] (1-indexed)
                                ^  ^  ^     (initial_lsits)
                 1:          a        b  c
                 2:       a     b  c
                 3:    a  b  c
        上記の順に a = max(b, c) を計算してセグメントツリーを構築する。
        ツリーとして見やすくするためにインデントすると次のようになる。

        seg._tree = [-,
                   3,
             2,    3,
          1, 2, 3, 0, (<- Filled with initial_list)
        ]
        """

        # Number of leaves (the smallest power of 2 that is greater than or equal to N)
        self._tree_width: Final = 1 << (len(initial_list) - 1).bit_length()

        self._evaluate: Final = evaluate

        # Initialize the tree with identity and initial_list
        self._tree = [identity] * 2 * self._tree_width
        self._tree[
            self._tree_width : self._tree_width + len(initial_list)
        ] = initial_list

        # Construct Segment Tree from bottom to top
        for parent_pos in reversed(range(self._tree_width)):
            left_child = self._tree[2 * parent_pos]
            right_child = self._tree[2 * parent_pos + 1]
            self._tree[parent_pos] = self._evaluate(left_child, right_child)

    def update(self, pos_to_be_updated: int, new_value) -> None:
        """
        Update the value at pos_to_be_updated to new_value

        Complexity: O(log N)

        Parameters:
        pos_to_be_updated : 更新する要素のインデックス (0-indexed)
        new_value         : 更新後の値
        """

        # Update the leaf
        pos = self._tree_width + pos_to_be_updated
        self._tree[pos] = new_value

        # Climbing up the tree (pos == 1 means root)
        while 1 < pos:
            parent_pos = pos >> 1
            sibling_pos = pos ^ 1
            self._tree[parent_pos] = self._evaluate(
                self._tree[pos], self._tree[sibling_pos]
            )
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
        For enumerate(seg._tree) = [(0, -),
                                  (1, 8),
                  (2, 4),         (3, 8),
          (4, 4), (5, 2), (6, 8), (7, 1),  # (0, 1, 2, 3 : original array index)
        ],

        >>> seg.query(0, 2)
        (0, 2) -> (4, 6) -> ()
        4
        """

        l_pos += self._tree_width
        r_pos += self._tree_width

        def right_child(pos: int) -> bool:
            return pos & 1 == 1  # odd

        result = self._tree[l_pos]
        while l_pos < r_pos:
            if right_child(l_pos):
                result = self._evaluate(result, self._tree[l_pos])

                # Go to right cousin
                l_pos += 1

            if right_child(r_pos):
                result = self._evaluate(result, self._tree[r_pos - 1])

            # Go to parent
            l_pos >>= 1
            r_pos >>= 1

        return result


class LazySegmentTree:
    """ """

    def __init__(
        self, initial_list: list, tree_op, tree_unit, lazy_op, lazy_unit, op
    ) -> None:
        """ """
        self._tree_op = tree_op
        self._tree_unit = tree_unit

        self._lazy_op = lazy_op
        self._lazy_unit = lazy_unit

        self._op = op

        self._num_of_leaves = 1 << (len(initial_list) - 1).bit_length()
        self._num_of_internal_nodes = self._num_of_leaves - 1
        self._tree_size = self._num_of_leaves << 1

        # Initialize the tree with identity and initial_list (1-indexed)
        self._tree_values = [self._tree_unit] * self._tree_size
        self._tree_values[
            self._num_of_leaves : self._num_of_leaves + len(initial_list)
        ] = initial_list

        # Construct Segment Tree from bottom to top
        for node_pos in reversed(range(1, self._num_of_internal_nodes + 1)):
            self._tree_values[node_pos] = self._tree_op(
                self._tree_values[Node(node_pos).left_child_pos()],
                self._tree_values[Node(node_pos).right_child_pos()],
            )

        # Lazy values (1-indexed)
        self._lazy_values = [self._lazy_unit] * self._tree_size

    def _nodes_to_be_propagated(self, l_node_pos: int, r_node_pos: int):
        """
        For query [l, r), return node indices that are propagated from the leaf to the root.

        Parameters:
        l_node_pos : 1-indexed
        r_node_pos : 1-indexed
        """
        l_node_pos = (l_node_pos // (l_node_pos & -l_node_pos)) >> 1
        r_node_pos = (r_node_pos // (r_node_pos & -r_node_pos)) >> 1

        while l_node_pos != r_node_pos:
            if r_node_pos < l_node_pos:
                yield l_node_pos
                l_node_pos = Node(l_node_pos).parent_pos()
            else:
                yield r_node_pos
                r_node_pos = Node(r_node_pos).parent_pos()

        while 1 <= l_node_pos:
            yield l_node_pos
            l_node_pos = Node(l_node_pos).parent_pos()

    def _is_leaf(self, node_pos: int) -> bool:
        """
        Judge whether the node is leaf or not.
        """
        return self._num_of_internal_nodes < node_pos

    def _offset(self, list_pos: int) -> int:
        """
        Convert the index of the list to the index of the tree.
        Note that the root node is 1.
        """
        return self._num_of_internal_nodes + 1 + list_pos

    def _covering_list_length(self, node_pos: int) -> int:
        """
        The number of leaves which the node has.

        Parameters:
        node_pos : 1-indexed (root is 1)
        """
        return self._num_of_leaves >> (node_pos.bit_length() - 1)

    def _propagate(self, node_pos: int) -> None:
        """
        Propagate the lazy value to the children nodes.
        """

        if not self._is_leaf(node_pos):
            # Propagate the lazy value to the left child
            l_child_pos = Node(node_pos).left_child_pos()
            self._lazy_values[l_child_pos] = self._lazy_op(
                self._lazy_values[l_child_pos], self._lazy_values[node_pos]
            )

            # Propagate the lazy value to the right child
            r_child_pos = Node(node_pos).right_child_pos()
            self._lazy_values[r_child_pos] = self._lazy_op(
                self._lazy_values[r_child_pos], self._lazy_values[node_pos]
            )

        self._tree_values[node_pos] = self._op(
            self._tree_values[node_pos],
            self._lazy_values[node_pos],
            self._covering_list_length(node_pos),
        )

        # Initialize the lazy value
        self._lazy_values[node_pos] = self._lazy_unit

    def _op_(self, node_pos, covering_list_length):
        return self._op(
            self._tree_values[node_pos],
            self._lazy_values[node_pos],
            covering_list_length,
        )

    def _recalculation(self, node_pos: int) -> None:
        """
        Recalculate the node values from the children values.
        """

        if self._is_leaf(node_pos):
            return

        covering_list_length = self._num_of_leaves >> node_pos.bit_length()
        # covering_list_length = self._covering_list_length(node_pos)

        l_child_pos = Node(node_pos).left_child_pos()
        r_child_pos = Node(node_pos).right_child_pos()

        # lazy_values も考慮するのは、区間更新の場合(?)
        self._tree_values[node_pos] = self._tree_op(
            self._op_(l_child_pos, covering_list_length),
            self._op_(r_child_pos, covering_list_length),
        )

    def update(self, l_list_pos, r_list_pos, new_value):
        """
        Update the value in [l_list_pos, r_list_pos).
        """

        l_node_pos = self._offset(l_list_pos)
        r_node_pos = self._offset(r_list_pos)

        (*poss,) = self._nodes_to_be_propagated(l_node_pos, r_node_pos)

        for pos in reversed(poss):
            self._propagate(pos)

        while l_node_pos < r_node_pos:
            if l_node_pos & 1:
                self._lazy_values[l_node_pos] = self._lazy_op(
                    self._lazy_values[l_node_pos], new_value
                )
                l_node_pos += 1

            if r_node_pos & 1:
                r_node_pos -= 1
                self._lazy_values[r_node_pos] = self._lazy_op(
                    self._lazy_values[r_node_pos], new_value
                )

            l_node_pos = Node(l_node_pos).parent_pos()
            r_node_pos = Node(r_node_pos).parent_pos()

        for pos in poss:
            self._recalculation(pos)

    def query(self, l_list_pos: int, r_list_pos: int):
        """
        Query the value in [l_list_pos, r_list_pos).
        """

        l_node_pos = self._offset(l_list_pos)
        r_node_pos = self._offset(r_list_pos)
        (*poss,) = self._nodes_to_be_propagated(l_node_pos, r_node_pos)
        print(l_node_pos, r_node_pos, poss)

        for node_pos in reversed(poss):
            self._propagate(node_pos)

        l_value = r_value = self._tree_unit
        covering_list_length = 1

        while l_node_pos < r_node_pos:
            if Node(l_node_pos).is_left_child():
                l_value = self._tree_op(
                    l_value, self._op_(l_node_pos, covering_list_length)
                )
                l_node_pos += 1

            if Node(r_node_pos).is_right_child():
                r_node_pos -= 1
                r_value = self._tree_op(
                    self._op_(r_node_pos, covering_list_length), r_value
                )

            l_node_pos = Node(l_node_pos).parent_pos()
            r_node_pos = Node(r_node_pos).parent_pos()
            covering_list_length <<= 1

        print(l_value, r_value)
        print(self._tree_values)
        return self._tree_op(l_value, r_value)
