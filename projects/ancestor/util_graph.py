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


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # set is O(1) time complexity --> no duplicates. Better time complexity than using a list or an array
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        If both exist, add a connection from v1 to v2
        """
        if v1 in self.vertices and v2 in self.vertices:

            self.vertices[v1].add(v2)
        else:
            # Python builtin exception -->
            raise IndexError("That vertex does not exits!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # Need to check if the bottom code is correct.
        return self.vertices[vertex_id]

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a queue/stack as appropriate
        stack = Stack()
        # Put the starting point in that
        # Enstack a list to use as our path
        stack.push([starting_vertex])
        # Make a set to keep track of where we have been
        visited = set()
        # While there is stuff in the stack/queue
        while stack.size() > 0:
            # Pop the first item
            path = stack.pop()
            # vertex = last item in the path
            vertex = path[-1]
            # If not visited
            if vertex not in visited:
                # If is the destination vertex in our path
                if vertex == destination_vertex:
                    # DO THE THING!
                    return path  # possibly return the thing
                # Add to visited
                visited.add(vertex)
                # For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    # Copy path to avoid pass by reference bug instead of passing the value. You are just copying over the original
                    # Makes a copy of path rather than reference
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)
