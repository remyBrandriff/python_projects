# Remy Brandriff
# CS499 - Bioinformatics
# Assignment 3
# UPGMA in Python with Newick string
# 03/29/19


def smallest(points):
    default = float("inf")

    x_coord = -1
    y_coord = -1

    # Find the smallest point to start with
    for i in range(len(points)):
        for j in range(len(points[i])):
            if points[i][j] < default:

                default = points[i][j]
                x_coord = i
                y_coord = j

    return x_coord, y_coord


# Join the two nodes
def join_nodes(nodes, x_coord, y_coord):
    if y_coord < x_coord:
        x_coord, y_coord = y_coord, x_coord

    # Join the labels in the first index
    nodes[x_coord] = "(" + nodes[x_coord] + "," + nodes[y_coord] + ")"

    # Delete the old one
    del nodes[y_coord]

    # print(nodes)


# Join the two points
def join_points(points, x_coord, y_coord):

    # Compare and swap if x_coord is larger
    if y_coord < x_coord:
        x_coord, y_coord = y_coord, x_coord

    # First we check the row and add the new point
    new_point = []

    for i in range(0, x_coord):
        new = (points[x_coord][i] + points[y_coord][i]) / 2
        new_point.append(new)

    points[x_coord] = new_point

    # Then we check the column
    for i in range(x_coord + 1, y_coord):
        new = (points[i][x_coord] + points[y_coord][i]) / 2
        points[i][x_coord] = new

    #  Get the rest of the values
    for i in range(y_coord + 1, len(points)):
        new = (points[i][x_coord] + points[i][y_coord]) / 2
        points[i][x_coord] = new

        # Remove the old point
        del points[i][y_coord]

    # And remove the old point
    del points[y_coord]

    # print(points)


# Run UPGMA clustering
def upgma(points, nodes):
    # Until we run out of nodes, perform UPGMA clustering by joining points and nodes
    while len(nodes) > 1:
        x_coord, y_coord = smallest(points)

        join_points(points, x_coord, y_coord)
        join_nodes(nodes, x_coord, y_coord)

    # Return the last node left, which should be all nodes combined
    return nodes[0]


# Initialize table and set the points
# Uses the example we did in class so I can troubleshoot
if __name__ == '__main__':

    nodes = []
    for i in range(ord("A"), ord("E") + 1):
        nodes.append(chr(i))

    points = [
        [],
        [3.6],
        [5.9, 3.8],
        [1.3, 5.4, 7.5],
        [1.1, 9.3, 3.4, 1]
    ]

    print("Original array: " + str(points))
    print("Original order: " + str(nodes))

    print(upgma(points, nodes) + ";")
