from collections import defaultdict as ddict


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def has_cycle(head):
    p = head
    cycle = 0
    while p is not None:
        print(p.data)
        # print(p.next)
        if not getattr(p, "visited", 0):
            setattr(p, "visited", 1)
        else:
            print("Here!")
            cycle = 1
            break

        p = p.next

    return cycle


def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road:
        return c_lib * n
    g, seen, ans = ddict(set), set(), 0
    for i, j in cities:
        g[i].add(j)
        g[j].add(i)

    def dfs(i):
        seen.add(i)
        return sum(dfs(j) for j in g[i] if j not in seen) + 1

    return sum((dfs(i) - 1) * c_road + c_lib for i in range(1, n + 1) if i not in seen)


if __name__ == '__main__':
    q1 = Node(1)

    # assert has_cycle(q1) == 0

    q2 = Node(2)
    q3 = Node(3)
    q4 = Node(4)
    q5 = Node(5)

    q1.next = q2
    q2.next = q3

    # assert has_cycle(q1) == 0
    # print(has_cycle(q1))

    q3.next = q4
    q4.next = q5
    q5.next = q3
    #
    assert has_cycle(q1) == 1
