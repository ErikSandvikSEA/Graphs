"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Nonexistent vertex")

    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            vertex = s.pop()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        visited.add(starting_vertex)
        print(starting_vertex)
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()
        while q.size() > 0:
            path = q.dequeue()
            last = path[-1]
            if last not in visited:
                if last == destination_vertex:
                    return path
                visited.add(last)
                for neighbor in self.get_neighbors(last):
                    neighbor_path = list(path)
                    neighbor_path.append(neighbor)
                    q.enqueue(neighbor_path)

    def dfs(self, starting_vertex, destination_vertex):
        s = Stack()
        s.push([starting_vertex])
        visited = set()
        while s.size() > 0:
            path = s.pop()
            first = path[-1]
            if first not in visited:
                if first == destination_vertex:
                    return path
                visited.add(first)
                for neighbor in self.get_neighbors(first):
                    neighbor_path = list(path)
                    neighbor_path.append(neighbor)
                    s.push(neighbor_path)

    def dfs_recursive(self, starting_vert, ending_vert, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(starting_vert)
        # path = path + [starting_vert] #subtly makes a copy of the path
        # more explicit way ↓
        path = list(path)  # make a copy
        path.append(starting_vert)

        if starting_vert == ending_vert:
            return path

        for neighbor in self.get_neighbors(starting_vert):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, ending_vert, visited, path)
                if new_path is not None:
                    return new_path

        return None  # if no path is found


sample = Graph()  # Instantiate your graph
sample.add_vertex("0")
sample.add_vertex("1")
sample.add_vertex("2")
sample.add_vertex("3")
sample.add_edge("0", "1")
sample.add_edge("1", "0")
sample.add_edge("0", "3")
sample.add_edge("3", "0")
# sample.add_edge("0", "4")  # No '4' vertex, should raise an Exception!
print("Sampler: ", sample.vertices)
print("--------------------------------")

if __name__ == "__main__":
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """
    print(graph.vertices)

    """
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    """
    graph.bft(1)

    """
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    """
    graph.dft(1)
    graph.dft_recursive(1)

    """
    Valid BFS path:
        [1, 2, 4, 6]
    """
    print(graph.bfs(1, 6))

    """
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    """
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
