import turtle


# this function will collect the Draper numbers for all stars,
# to be used later in the program
def all_drapers(file):
    drapers = []
    fh = open(file, "r")
    for line in fh:
        line = line.split(" ")
        drapers.append(line[3])
    return drapers


# this function will operate on a file to retrieve x and y coordinates,
# magnitudes, and Draper numbers for all stars in the stars.txt file
def read_coords(file):
    coords = {}
    mags = {}
    drapers = {}
    fh = open(file, "r")
    for line in fh:
        line = line.strip('\n').split(" ")
        coords[line[3]] = [float(line[0]), float(line[1])]
        mags[line[3]] = float(line[4])
        name = ""
        for i in range(6, len(line)):
            try:
                if line[i][-1] != ";":
                    name = name + line[i] + " "
                    if line[i] == line[-1]:
                        name = name.strip()
                        drapers[name] = line[3]
                        name = ""
                else:
                    name = name + line[i].rstrip(';')
                    drapers[name] = line[3]
                    name = ""
            except IndexError:
                pass
    return (coords, mags, drapers)


# this function will draw a square of a given size in turtle graphics
def draw_square(size):
    turtle.begin_fill()
    turtle.seth(270)
    turtle.pd()
    turtle.fd(size/2)
    turtle.right(90)
    turtle.fd(size/2)
    turtle.right(90)
    turtle.fd(size)
    turtle.right(90)
    turtle.fd(size)
    turtle.right(90)
    turtle.fd(size)
    turtle.right(90)
    turtle.fd(size)
    turtle.end_fill()


# this function will use the magnitude of each star to draw a square
# of a certain size, representing that star
def plot_by_magnitude(picture_size, coordinates_dict, magnitudes_dict):
    length = int(picture_size / 2)
    turtle.bgcolor("black")
    turtle.color("white")
    for number in all_drapers:
        mag = magnitudes_dict[number]
        star_size = round(10.0 / (mag + 2))
        if star_size > 8:
            star_size = 8
        x = coordinates_dict[number][0] * length
        y = coordinates_dict[number][1] * length
        turtle.pu()
        turtle.setpos(x, y)
        draw_square(star_size)


# this function will read a constellation file and assemble the data into
# dictionaries to be used for drawing out those constellations
def read_constellation_lines(file):
    star_names = {}
    fh = open(file, "r")
    for line in fh:
        line = line.strip('\n').split(',')
        if line[0] not in star_names:
            star_names[line[0]] = [line[1]]
        else:
            star_names[line[0]].append(line[1])
        if line[1] not in star_names:
            star_names[line[1]] = [line[0]]
        else:
            star_names[line[1]].append(line[0])
    return star_names


# this function will take the data obtained above and use it to draw lines
# between the appropriate stars to form a constellation
def plot_constellations(pic_size, star_names, star_coords, constellations):
    length = int(pic_size / 2)
    turtle.color("yellow")
    for key in constellations:
        init_name = key
        init_draper = star_names[init_name]
        init_x = star_coords[init_draper][0] * length
        init_y = star_coords[init_draper][1] * length
        turtle.pu()
        turtle.setpos(init_x, init_y)
        for star in constellations[key]:
            end_name = star
            end_draper = star_names[end_name]
            end_x = star_coords[end_draper][0] * length
            end_y = star_coords[end_draper][1] * length
            turtle.pd()
            turtle.setpos(end_x, end_y)
            turtle.pu()
            turtle.setpos(init_x, init_y)

# execute all of the functions to assemble the data structures for the stars
stars = read_coords("stars.txt")
coordinates = stars[0]
magnitudes = stars[1]
drapers = stars[2]
all_drapers = all_drapers("stars.txt")

# assemble a dictionary of connected stars for each constellation
big_dipper = read_constellation_lines("big_dipper.txt")
bootes = read_constellation_lines("bootes.txt")
cassiopeia = read_constellation_lines("cassiopeia.txt")
cygnet = read_constellation_lines("cygnet.txt")
gemini = read_constellation_lines("gemini.txt")
hydra = read_constellation_lines("hydra.txt")
ursa_minor = read_constellation_lines("ursa_minor.txt")
ursa_major = read_constellation_lines("ursa_major.txt")

turtle.tracer(1)
turtle.speed(50)

# draw out the stars based on the data obtained above
plot_by_magnitude(800, coordinates, magnitudes)

# draw out the each of the constellations given in the data obtained above
plot_constellations(800, drapers, coordinates, big_dipper)
plot_constellations(800, drapers, coordinates, bootes)
plot_constellations(800, drapers, coordinates, cassiopeia)
plot_constellations(800, drapers, coordinates, cygnet)
plot_constellations(800, drapers, coordinates, gemini)
plot_constellations(800, drapers, coordinates, hydra)
plot_constellations(800, drapers, coordinates, ursa_major)
plot_constellations(800, drapers, coordinates, ursa_minor)
