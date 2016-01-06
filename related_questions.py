__author__ = "Albert Yu"

# https://www.quora.com/challenges#related_questions


class Vertex(object):
    """
    Vertex object which represents the questions
    """
    def __init__(self, label, time):
        self.label = label  # int 1 through N, where N is the total number of vertices
        self.time = time  # int
        self.neighbors = dict()
        self.degree = 0  # number of neighbors
        self.visited = False

    def add_neighbor(self, vertex):
        self.neighbors[vertex] = True
        self.degree += 1
        vertex.neighbors[self] = True
        vertex.degree += 1

    def remove_neighbor(self, neighbor):
        if self.neighbors[neighbor] is None:
            return -1  # stub
        else:
            self.neighbors[neighbor] = False
            self.degree -= 1
            neighbor.neighbors[self] = False
            neighbor.degree -= 1

    def is_leaf(self):
        if self.degree == 1:
            return True
        return False

    def is_first(self):
        """
        Indicates whether a vertex is the first vertex to be "visited" in a search algorithm
        :return: boolean
        """
        for neighbor in self.neighbors:
            if neighbor.visited is True:    # if any of a vertex's neighbors has already been visited,
                return False                # then it's not the first
        return True

    def iterate(self):
        """
        Implement DFS to find path from vertex to leaf
        :return:
        """
        self.visited = True
        if self.is_leaf() is True and self.is_first() is False:
            return [self]
        else:
            all_paths = []
            for neighbor in self.neighbors:
                current_path = [self]
                if neighbor.visited is False:
                    current_path.extend(neighbor.iterate())
                    all_paths.extend(current_path)

            return all_paths


class Tree(object):
    def __init__(self):
        self.vertices = dict()
        self.label_to_obj = dict()  # so entire vertex object can be accessed via just the label
        self.size = 0

    def add(self, vertex):
        """
        Adds a vertex to the tree
        :param vertex:
        :return: None
        """
        self.vertices[vertex] = vertex.neighbors
        self.label_to_obj[vertex.label] = vertex
        self.size += 1

    def remove(self, vertex):
        """
        Removes a vertex from the tree
        :param vertex:
        :return:
        """
        if self.vertices[vertex] is None:
            raise KeyError
        else:
            for neighbor in vertex.neighbors:
                vertex.remove_neighbor(neighbor)
            self.vertices.pop(vertex)
            self.label_to_obj.pop(vertex)
            self.size -= 1

    def connect(self, vertex_1, vertex_2):
        """
        Connects two vertices
        :param vertex_1:
        :param vertex_2:
        :return:
        """
        if self.vertices[vertex_1] is None or self.vertices[vertex_2] is None:
            raise KeyError
        else:
            vertex_1.add_neighbor(vertex_2)

    def disconnect(self, vertex_1, vertex_2):
        """
        Disconnects two vertices
        :param vertex_1:
        :param vertex_2:
        :return:
        """
        if self.vertices[vertex_1] is None or self.vertices[vertex_2] is None:
            raise KeyError
        else:
            vertex_1.remove_neighbor(vertex_2)

    def num_leaves(self):
        """
        Counts the number of leaves
        :return:
        """
        count = 0
        for vertex in self.vertices:
            if vertex.is_leaf() is True:
                count += 1
        return count

    def clear_visits(self):
        """
        Marks all vertices as not visited
        :return:
        """
        for vertex in self.vertices:
            vertex.visited = False


def calc_path_time(path):
    """
    Given a list of vertex objects, this will calculate the total time it will take to traverse them
    :param path:
    :return: tuple[0], the path's starting vertex
             tuple[1], the path's ending vertex
             tuple[2], the time it takes to traverse the path
    """
    time = 0
    for vertex in path:
        time += vertex.time
    return path[0], path[len(path)-1], time


def find_max_time(paths):
    """
    Given a list of paths of vertices, returns the starting vertex of the path
    :param paths:
    :return: tuple[0], starting_vertex, the starting vertex of the path that gives that max time
             tuple[1], ending_vertex, the ending vertex of the path
    """
    starting_vertex = None
    ending_vertex = None
    max_time = 0
    for path in paths:
        if max_time < calc_path_time(path)[2]:
            starting_vertex = calc_path_time(path)[0]
            ending_vertex = calc_path_time(path)[1]
            max_time = calc_path_time(path)[2]
    return starting_vertex, ending_vertex


def main():
    input_data = []
    with open('sample.txt', 'r') as f:
        data = f.readlines()

        for line in data:
            numbers = line.split()
            integers = []
            for number in numbers:
                integers.append(int(number))
            input_data.append(integers)

    num_vertices = input_data[0][0]  # line 1 of txt file
    time_values = input_data[1]  # line 2
    edges = input_data[2:len(input_data) - 1]  # lines 3 to N + 1
    tree = Tree()
    i = 0
    while i < num_vertices:
        tree.add((Vertex(i + 1, time_values[i])))
        i += 1
    for pair in edges:
        tree.connect(tree.label_to_obj[pair[0]], tree.label_to_obj[pair[1]])

    leaves = [vertex for vertex in tree.vertices if vertex.is_leaf() is True]
    paths = []
    for leaf in leaves:
        paths.append(leaf.iterate())
        tree.clear_visits()
    the_vertices_we_want = find_max_time(paths)
    path_we_want = None
    for path in paths:
        if path[0] == the_vertices_we_want[0] and path[len(path) - 1] == the_vertices_we_want[1]:
            path_we_want = path

    vertex_we_want = path_we_want[len(path_we_want)//2]
    print(vertex_we_want.label)


if __name__ == "__main__":
    main()


