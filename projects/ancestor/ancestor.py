from ancestor_util import Stack, Queue


def get_parents(ancestors, node):
    parents = []
    for ancestor in ancestors:
        if node == ancestor[1]:
            parents.append(ancestor[0])

    return parents


def earliest_ancestor(ancestors, starting_node):
    if get_parents(ancestors, starting_node) == []:
        return -1
    q = Queue()
    q.enqueue(starting_node)
    ancestor_list = []
    visited = set()
    depth = 0
    while q.size() > 0:
        v = q.dequeue()
        if v not in visited:
            visited.add(v)
            for parent in get_parents(ancestors, v):
                if len(get_parents(ancestors, parent)) == 0:
                    ancestor_list.append((parent, depth + 1))
                else:
                    ancestor_list.append((parent, depth + 1))
                q.enqueue(parent)
            depth += 1

    if len(ancestor_list) == 1:
        return ancestor_list[-1][0]
    if ancestor_list[-1][1] == ancestor_list[-2][1]:
        return min(ancestor_list[-2][0], ancestor_list[-1][0])
    else:
        return ancestor_list[-1][0]


sample = [
    (1, 3),
    (2, 3),
    (3, 6),
    (5, 6),
    (5, 7),
    (4, 5),
    (4, 8),
    (8, 9),
    (11, 8),
    (10, 1),
]

print(earliest_ancestor(sample, 1))
# print(get_parents(sample, 8))
