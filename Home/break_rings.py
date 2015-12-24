"""
A blacksmith gave his apprentice a task, ordering them to make a selection of
rings. The apprentice is not yet skilled in the craft and as a result of this,
some (to be honest, most) of rings came out connected together. Now he’s asking
for your help separating the rings and deciding how to break enough rings to
free so as to get the maximum number of rings possible.

All of the rings are numbered and you are told which of the rings are connected.
This information is given as a sequence of sets. Each set describes the
connected rings. For example: {1, 2} means that the 1st and 2nd rings are
connected. You should count how many rings we need to break to get the maximum
of separate rings. Each of the rings are numbered in a range from 1 to N, where
N is total quantity of rings.

https://checkio.s3.amazonaws.com/task/media/0d98b24304034e2e9017ba00fc51f6e3/example-rings.svg

In the above image you can see the connections:
({1,2},{2,3},{3,4},{4,5},{4,6},{6,5}).
The optimal solution here would be to break 3 rings, making 3 full and separate
rings. So the result is 3.
Input: Information about the connected rings as a tuple of sets with integers.
Output: The number of rings to break as an integer.
Precondition:
all(len(s) == 2 for s in rings)
sorted(reduce(set.union, rings)) == list(range(1, max(reduce(set.union, rings)) + 1))
"""

"""
Strategy:
1. Count endpoints (rings with only one connection).
2. If 0 endpoints, cut one link and go to step 1.

Alternate strategy:
1. Make a dict with the number of connections to each ring.
2. Start by cutting connections to rings with the least connections.
"""

def break_rings(rings):
    return 1

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
