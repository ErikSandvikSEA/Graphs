from ancestor_util import Ancestor_Stack, Ancestor_Queue
from queue import Queue


def get_parents(ancestors, node):
    parents = []
    for ancestor in ancestors:
        if node == ancestor[1]:
            parents.append(ancestor[0])

    return parents


def earliest_ancestor_1(ancestors, starting_node):
    if get_parents(ancestors, starting_node) == []:
        return -1
    q = Ancestor_Queue()
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


def earliest_ancestor_2(ancestors, starting_node):
    families = {}  # child is the key, parents are the values
    # build hashtable
    for fam in ancestors:
        if fam[1] in families:
            families[fam[1]].add(fam[0])
        else:
            families[fam[1]] = {fam[0]}

        # set the vals to a set that we can add to - if there aren't any parents, the value is an empty set
        if fam[0] not in families:
            families[fam[0]] = set()
    if len(families[starting_node]) == 0:
        return -1
    next_generation = {starting_node}
    while len(next_generation) > 0:
        current = next_generation
        next_generation = set()
        for node in current:
            next_generation = next_generation | families[node]
        # print(next_generation)
    return min(current)


def earliest_ancestor_3(ancestors, starting_node):
    graph = {}
    for node in ancestors:
        if node[1] not in graph:
            graph[node[1]] = [node[0]]
        else:
            graph[node[1]].append(node[0])

    if starting_node not in graph:
        return -1

    q = Queue()
    q.put([starting_node])

    found_ancestors = []

    while not q.empty():
        path = q.get()
        v = path[-1]

        if v not in graph:
            found_ancestors.append(path)
        else:
            for parent in graph[v]:
                q.put(path + [parent])

    if len(found_ancestors) == 1:
        return found_ancestors[0][-1]

    else:
        max_length = max([len(path) for path in found_ancestors])
        return min([path[-1] for path in found_ancestors if len(path) == max_length])


earliest_ancestor = earliest_ancestor_1

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

earliest_ancestor(sample, 1)
# print(get_parents(sample, 8))
