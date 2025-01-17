import bisect

[_], A = [[*map(int, l.split())] for l in open(0)]


def longest_increasing_subsequence(sequence):
    """
    O(n log n)
    """
    lis = [sequence[-1]]

    for element in sequence:
        if lis[-1] < element:
            lis.append(element)
        else:
            # Exchange the element with the smallest element larger than it
            lis[bisect.bisect_left(lis, element)] = element
    return len(lis)


print(longest_increasing_subsequence(A))
