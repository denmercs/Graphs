"""
1. Understanding the problem
- 1 input data
- formatted as list of (parent, child) pairs, 
- each individual is assigned a unique integer identifier
- needs to return the earliest known ancestor from the one at the farthest distance form the input individual
- if tie, return the lowerst numeric id
- if no parents, the function should return -1


    10
    /
    1   2   4  11
    \ /   / \ /
    3   5   8
    \ / \   \
    6   7   9

Example input
  6

(1, 3)
(2, 3)
(3, 6)
(5, 6)
(5, 7)
(4, 5)
(4, 8)
(8, 9)
(11, 8)
(10, 1)
Example output
  10


"""
from util_graph import Stack, Graph


def earliest_ancestor(ancestors, starting_node):
    tree = Graph()

    for ancestor in ancestors:
        for node in ancestor:
            tree.add_vertex(node)

    for ancestor in ancestors:
        tree.add_edge(ancestor[1], ancestor[0])
    print("Tree", tree.vertices)

    # default length to check the length of path list against
    longest_path = 1
    # counter for storing storing the last node
    last_node = 0
    # passing the vertices by reference
    ancestor_vert = tree.vertices

    # Iterate through the vertices of the ancestorTree
    for i in ancestor_vert:
        # i = individual nodes/vertices added using add_vert()
        # returns a list of nodes and sets the list to the variable path
        path = tree.dfs(starting_node, i)
        # print("path list loop", path)

        # If path is not = to None and the length of the path list in greater that longest_path which defaults to the value integer 1
        if path is not None and len(path) > longest_path:
            # set longest_path = length of the path
            longest_path = len(path)
            print("longest_path", longest_path)
            # last node is = to last node/vertice of the longest_path
            last_node = i
            print("last_node", last_node)
        # I was missing that longest_path defaults to 1.
        # If path list is empty and longest_path is set to default of 1
        elif not path and longest_path == 1:
            # print("empty", path)
            # print("elif path", longest_path)
            # set last_node to -1
            last_node = -1

    # print("Out of for loop", last_node)
    return last_node


# print("function", earliest_ancestor(ancestor_data, 6))