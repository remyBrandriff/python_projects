__author__ = 'jmc789'''

import turtle

coordinates_dict = {}
magnitude_dict = {}

file = open("test.txt", "r")

def read_coords(file):

    for line in file:

        file_line = line.split(" ")
        x_coord = file_line[0]
        y_coord = file_line[1]
        HD = file_line[3]
        Mag = file_line[4]
        Name = file_line[6:]
        name = (" ").join(Name)
        Name = name.split(";")
    coordinates_dict = {HD: (x_coord, y_coord)}
    magnitude_dict = {HD: Mag}
    #Constellation_dict = {Name: HD}
    stars_info = (coordinates_dict, magnitude_dict)
    return stars_info

def plot_plain_stars(picture_size, coordinates_dict):
    turtle.setup(picture_size, picture_size)
    turtle.bgcolor('black')
    turtle.pencolor('white')
    turtle.fillcolor('white')


    for HD in coordinates_dict:
        coords = coordinates_dict(HD)
        x = coords[0]
        y = coords[1]
        print(x)
        print(y)

        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.fd(1)
        turtle.right(90)
        turtle.fd(1)
        turtle.right(90)
        turtle.fd(1)
        turtle.right(90)
        turtle.fd(1)
        turtle.end_fill()



#def plot_by_magnitude(picture_size, coordinates_dict, madnitudes_dict):

read_coords(file)
plot_plain_stars(300, coordinates_dict)

turtle.exitonclick()