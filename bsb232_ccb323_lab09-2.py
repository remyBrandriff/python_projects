# Lab 09 - Draw Stars
# Remy Brandriff - Chloe Bates
# bsb232 - ccb323
# Section 002
'''for i in lines:
    x = i[0]
    y = i[1]
    hdn = i[3]
    mag = i[4]
    name = i[6:]

    coords_dict[i]={hdn}'''

import turtle

tuple = ({}, {}, {})
coords_dict = tuple[0]
mag_dict = tuple[1]
hdn_dict = tuple[2]

def read_coords(lines):
    for i in lines:
        stripped = i.strip()
        splitted = stripped.split(" ")
        x = splitted[0]
        y = splitted[1]
        hdn = splitted[3]
        mag = splitted[4]
        name = splitted[6:]
        names = " ".join(name)

        if len(names) > 1:
            two_names = names.split(";")
            for i in two_names:
                hdn_dict[i] = (hdn)

        coords_dict[hdn] = (x,y)
        mag_dict[hdn] = (float(mag))

    return(tuple)

def plot_plain_stars(picture_size, coordinates_dict):
    turtle.setup(picture_size, picture_size)
    turtle.bgcolor("black")
    turtle.pencolor("white")
    turtle.fillcolor("white")

    for i in coordinates_dict:
        turtle.goto(i[0], i[1])
        turtle.pendown()
        turtle.fd(2)
        turtle.rt(90)
        turtle.fd(2)
        turtle.rt(90)
        turtle.fd(2)
        turtle.rt(90)
        turtle.fd(2)
        turtle.hideturtle()
        turtle.exitonclick()



def main():
    file = open("stars.txt", "r")
    lines = file.readlines()
    print(read_coords(lines))

    plot_plain_stars(500, coords_dict)

    #print(coords_dict['28'])

main()