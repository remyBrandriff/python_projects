__author__ = 'bsb232'
# Brittany Brandriff and Austin Collins
# November 9, 2015

import turtle

turtle.setup(300,300)
# turtle.penup()
# turtle.goto(10,10)
# turtle.tracer(0)
turtle.bgcolor("black")
turtle.pencolor("white")

def read_coords(star_file):

    star_file.split(' ')

    x_coord = star_file[0]
    y_coord = star_file[1]
    HD = star_file[3]
    magnitude = star_file[4]
    name = star_file[6]

    coordinates_dict = { HD: (x_coord, y_coord)}
    magnitude_dict = { HD: magnitude }
    constellation_dict = { name: HD }
    stars_info = (coordinates_dict, magnitude_dict, constellation_dict)
    return stars_info
#
# def plot_plain_stars(picture_size, coordinates_dict):
#
#     return
#
#
# def plot_by_magnitude(picture_size, coordinates_dict, magnitudes_dict):
#     star_size = round(10.0/(magntitude+2))
#     return


star_file = open('test_stars.txt', 'r')

read_coords(star_file)
# plot_plain_stars(picture_size, coordinates_dict)
# plot_by_magnitude(picture_size, coordinate_dict, magnitude_dict)

turtle.exitonclick()