import pytest
from .main import SegmentTree, LazySegmentTree

# ---------------------------
# Segment Tree


def test_segment_tree_normal():
    #        0, 1, 2, 3, 4, 5
    array = [3, 5, 2, 7, 1, 4]

    segment_tree = SegmentTree(initial_list=array, evaluate=min, identity=10**9)

    assert segment_tree.query(0, 1) == 3
    assert segment_tree.query(1, 2) == 5
    assert segment_tree.query(2, 3) == 2
    assert segment_tree.query(3, 4) == 7
    assert segment_tree.query(4, 5) == 1
    assert segment_tree.query(5, 6) == 4

    assert segment_tree.query(0, 2) == 3
    assert segment_tree.query(1, 3) == 2
    assert segment_tree.query(2, 4) == 2
    assert segment_tree.query(3, 5) == 1
    assert segment_tree.query(4, 6) == 1

    assert segment_tree.query(0, 3) == 2
    assert segment_tree.query(1, 4) == 2
    assert segment_tree.query(2, 5) == 1
    assert segment_tree.query(3, 6) == 1

    assert segment_tree.query(0, 4) == 2
    assert segment_tree.query(1, 5) == 1
    assert segment_tree.query(2, 6) == 1

    assert segment_tree.query(0, 5) == 1
    assert segment_tree.query(1, 6) == 1

    assert segment_tree.query(0, 6) == 1

    segment_tree.update(1, 1)
    # array = [3, 1, 2, 7, 1, 4]

    assert segment_tree.query(0, 1) == 3
    assert segment_tree.query(1, 2) == 1
    assert segment_tree.query(2, 3) == 2
    assert segment_tree.query(3, 4) == 7

    assert segment_tree.query(0, 2) == 1
    assert segment_tree.query(1, 3) == 1
    assert segment_tree.query(2, 4) == 2

    assert segment_tree.query(0, 3) == 1
    assert segment_tree.query(1, 4) == 1


def test_lazy_segment_tree_normal():
    #        0, 1, 2, 3, 4, 5
    array = [3, 5, 2, 7, 1, 4]

    def op(a, b, k):
        return min(a, b)

    segment_tree = LazySegmentTree(
        initial_list=array,
        tree_op=min,
        tree_unit=10**9,
        lazy_op=min,
        lazy_unit=10**9,
        op=op,
    )

    assert segment_tree.query(0, 1) == 3
    assert segment_tree.query(1, 2) == 5
    # assert segment_tree.query(2, 3) == 2
    # assert segment_tree.query(3, 4) == 7
    # assert segment_tree.query(4, 5) == 1
    # assert segment_tree.query(5, 6) == 4

    # assert segment_tree.query(0, 2) == 3
    # assert segment_tree.query(1, 3) == 2
    # assert segment_tree.query(2, 4) == 2
    # assert segment_tree.query(3, 5) == 1
    # assert segment_tree.query(4, 6) == 1

    # assert segment_tree.query(0, 3) == 2
    # assert segment_tree.query(1, 4) == 2
    # assert segment_tree.query(2, 5) == 1
    # assert segment_tree.query(3, 6) == 1

    # assert segment_tree.query(0, 4) == 2
    # assert segment_tree.query(1, 5) == 1
    # assert segment_tree.query(2, 6) == 1

    # assert segment_tree.query(0, 5) == 1
    # assert segment_tree.query(1, 6) == 1

    # assert segment_tree.query(0, 6) == 1

    # segment_tree.update(1, 1, 1)
    # # array = [3, 1, 2, 7, 1, 4]

    # assert segment_tree.query(0, 1) == 3
    # assert segment_tree.query(1, 2) == 1
    # assert segment_tree.query(2, 3) == 2
    # assert segment_tree.query(3, 4) == 7

    # assert segment_tree.query(0, 2) == 1
    # assert segment_tree.query(1, 3) == 1
    # assert segment_tree.query(2, 4) == 2

    # assert segment_tree.query(0, 3) == 1
    # assert segment_tree.query(1, 4) == 1
