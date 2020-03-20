"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue
        q = Queue()
        # Enqueue the starting vertex
        q.enqueue(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # Check if it's been visited
            # If it hasn't been visited
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Enqueue all it's neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack
        s = Stack()
        # Push the starting vertex
        s.push(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # Check if it's been visited
            # If it hasn't been visited
            if v not in visited:
                print(v)
                # Mark it as visited
                visited.add(v)
                # Push all it's neighbors
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, v=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if v is None:
            v = set()

            # Check if the node has been visited
            # If not
            # Mark it as visited
            # Call defs_recursive on each neighbor
        if starting_vertex not in v:
            print(starting_vertex)
            v.add(starting_vertex)
            children = self.get_neighbors(starting_vertex)
            for child in children:
                self.dft_recursive(child, v)




    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        q = Queue()
        # Enqueue a path to the starting vertex
        q.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()

        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first path
            path = q.dequeue()
            # grab the vertex from the end of the path
            vertex = path[-1]
            # check if it has been visited
            # If it hasn't been visited
            if vertex not in visited:
                # Mark it as visited
                visited.add(vertex)
                # Check if it's the target
                if vertex == destination_vertex:
                    # if so return the path
                    return path
                else:
                    # enqueue a path to all it's neighbors
                    for child in self.get_neighbors(vertex):
                        # Make a copy of the path
                        new_path = list(path)
                        new_path.append(child)
                        # enqueue the copy
                        q.enqueue(new_path)






    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a queue
        s = Stack()
        # Push a path to the starting vertex
        s.push([starting_vertex])
        # Create a set to store visited vertices
        visited = set()

        # While the stack is not empty
        while s.size() > 0:
            # Pop the first path
            path = s.pop()
            # grab the vertex from the end of the path
            vertex = path[-1]
            # check if it has been visited
            # If it hasn't been visited
            if vertex not in visited:
                # Mark it as visited
                visited.add(vertex)
                # Check if it's the target
                if vertex == destination_vertex:
                    # if so return the path
                    return path
                else:
                    # enqueue a path to all it's neighbors
                    for child in self.get_neighbors(vertex):
                        # Make a copy of the path
                        new_path = list(path)
                        new_path.append(child)
                        # push the copy
                        s.push(new_path)

    def dfs_recursive(self, starting_vertex, why):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        papa_path = []

        def recursion(v, num, stack=None, visited=None):
            if stack is None:
                stack = [[v]]

            if visited is None:
                visited = set()

            # Create a set to store visited vertices
            # Get path
            path = stack.pop()
            # Get last element of path
            last = path[-1]
            # check if not visited
            if last not in visited:
                # check if is destination
                visited.add(last)
                if last == why:
                    papa_path.append(path)
                else:
                    # copy path and add children to it
                    for child in self.get_neighbors(v):
                        new_path = list(path)
                        new_path.append(child)
                        stack.append(new_path)
                        recursion(child, num, stack, visited)

        recursion(starting_vertex, why)
        return papa_path[0]


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
    print(graph.vertices)

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
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    #print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    #print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
