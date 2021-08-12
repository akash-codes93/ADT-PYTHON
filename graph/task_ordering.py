"""
@url: https://leetcode.com/problems/course-schedule/submissions/
"""

from itertools import permutations
from collections import defaultdict


def is_valid(order, constraints):
    status = True
    for constraint in constraints:
        for task in constraints[constraint]:
            if order.index(task) < order.index(constraint):
                status = False
                break
    return status


def kahns_algorithm(v, e):
    # to keep in/ out of each vertex
    e_out = defaultdict(set)
    e_in = defaultdict(set)

    def link(head, tail):
        e_out[tail].add(head)
        e_in[head].add(tail)

    def unlink(head, tail):
        e_out[tail].remove(head)
        e_in[head].remove(tail)

    indegree = lambda v: len(e_in[v])
    outdegree = lambda v: len(e_out[v])

    # to check if vertex has dependency
    source = lambda v: indegree(v) == 0

    # creating DAG using constraints
    for tail in e:
        for head in e[tail]:
            link(head, tail)

    l = []
    # to find vertices with no dependencies -- initial queue
    s = set(filter(source, v))

    while s:
        tail = s.pop()
        # adding tail to the topological ordering
        l.append(tail)
        # tuple because set might change during iteration and give RuntimeError
        for head in tuple(e_out[tail]):
            unlink(head, tail)
            if source(head):
                s.add(head)

    no_cycles = all(
        indegree(each_v) == 0 and outdegree(each_v) == 0 for each_v in v
    )

    if no_cycles:
        print(l)


def main(optimised=True):
    """
    brute force: checking for constraints in all the permutations
                 Time complexity: O(n!*n^2)
Topological ordering: putting all nodes in straight line such that all the edges point towards the right
in a directed graph.
Only a DAG (directed acyclic graph) have a topological ordering.
There can be different topological ordering for same DAG.
Kahn's Algorithm:
Start removing nodes from the from the graph which has no dependencies (meaning no edges into that node) and add them
to the topological ordering.
Additional info to execute the algo:
- Incoming degree of each node
- Queue with nodes having 0 degree
Time complexity: O(V + E)
    :return:
    """
    constraints = {
        "E": {"A"},
        "D": {"B", "C", "E"},
        "B": {"C"},
    }

    tasks = ['A', 'B', 'C', 'D', 'E']

    if optimised:
        kahns_algorithm(v=tasks, e=constraints)
    else:  # brute force
        for order in permutations(tasks, len(tasks)):
            if is_valid(order, constraints):
                print(order)


if __name__ == '__main__':
    main()
