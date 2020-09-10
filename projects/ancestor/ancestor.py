class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):
    # build the graph
    familyTree = Graph()
    for relation in ancestors:
        familyTree.add_vertex(relation[0])
        familyTree.add_vertex(relation[1])
        familyTree.add_edge(relation[1], relation[0])

    # traversal the graph and find the ealiest_ancestor
    familyTree_q = Queue()
    familyTree_q.enqueue([starting_node])

    # return -1 if there is no ancester
    earliestAncestor = -1

    pathLength = 1

    while familyTree_q.size() > 0:
        path = familyTree_q.dequeue()
        farthest = path[-1]
        if (len(path) >= pathLength and farthest < earliestAncestor) or len(path) > pathLength:
            earliestAncestor = farthest
            pathLength = len(path)

        for neighbor in familyTree.get_neighbors(farthest):
            new_path = list(path)
            new_path.append(neighbor)
            familyTree_q.enqueue(new_path)
    return earliestAncestor


a = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
     (11, 5), (11, 8), (8, 9), (4, 8), (10, 1)]
print(earliest_ancestor(a, 1))
