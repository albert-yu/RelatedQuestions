from related_questions import *
__author__ = "Albert Yu"

# https://www.quora.com/challenges#related_questions


def main():
    input_data = []
    line_1 = int(input())
    input_data.append(line_1)
    old_line_2 = input().split()
    line_2 = []
    for number in old_line_2:
        line_2.append(int(number))
    input_data.append(line_2)
    last_line = input()
    while len(last_line) > 0:
        numbers = last_line.split()
        integers = []
        for number in numbers:
            integers.append(int(number))
        input_data.append(integers)
        last_line = input()

    num_vertices = line_1  # line 1 of txt file
    time_values = line_2  # line 2
    edges = input_data[2:len(input_data)]  # lines 3 to N + 1
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


