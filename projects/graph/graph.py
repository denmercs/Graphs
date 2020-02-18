"""
Simple graph implementation
"""
from util import Queue, Stack  # These may come in handy


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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a stack/queue as appropriate
        # using a queue because its first-in, first out
        queue = Queue()
        # Put the starting point in that
        queue.enqueue(starting_vertex)
        # Make a set to keep track of where we have been
        visited = set()
        # While there is stuff in the stack/queue
        while queue.size() > 0:
            # Pop the first item
            vertex = queue.dequeue()
            # If not visited
            if vertex not in visited:
                # DO THE THING!
                print(vertex)
                # Add to visited
                visited.add(vertex)
                # For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    # Add that edge to the stack/queue
                    queue.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack/queue as appropriate
        stack = Stack()
        # Put the starting point in that
        stack.push(starting_vertex)
        # Make a set to keep track of where we have been
        visited = set()
        # While there is stuff in the stacl/queue
        while stack.size() > 0:
            # Pop the first item
            vertex = stack.pop()
            # If not visited
            if vertex not in visited:
                # DO THE THING!
                print(vertex)
                # Add to visited
                visited.add(vertex)
                # For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    # Add that edge to the stack/queue
                    stack.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # This is creating a stack because this is recursion

        # base case
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue/queue as appropriate
        queue = Queue()
        # Put the starting point in that
        # Enstack a list to use as our path
        queue.enqueue([starting_vertex])
        # Make a set to keep track of where we have been
        visited = set()
        # While there is stuff in the stack/queue
        while queue.size() > 0:
            # Pop the first item
            path = queue.dequeue()
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
                    queue.enqueue(new_path)

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

    def dfs_recursive(self, starting_vertex, target_value, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        # base case
        if visited is None:
            visited = set()
        # base case
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == target_value:
            return path
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(
                    child_vert, target_value, visited, path)
                if new_path:
                    return new_path
        return None  # The returns are catching if the target doesn't exist


if __name__ == '__main__':
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

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print("Printing graph.vertices")
    print(graph.vertices)

    # This will only tell us a answer when it prints out

    '''
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
    '''
    print("Running bft")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # This will only tell us a single answer when it prints out. The result of a dft is a minimum spanning tree, which gives the shortest connection between all the nodes: minimum spanning forest
    print("Running dft")
    graph.dft(1)
    print("Running dft_recursive")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("Running graph.bfs")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("Running dfs")
    print(graph.dfs(1, 6))
    print("Running dfs_recursive")
    print(graph.dfs_recursive(1, 6))
