import sys

if __name__ == '__main__':

    if len(sys.argv) < 2:
        input_file = "./input.txt"
    else:
        input_file = sys.argv[1]

    x_array = []
    y_array = []

    print(type(x_array))

    # Open input file
    with open(input_file) as f:
        # For source rectangles
        rect_array = []

        # Coordinates arrays will represent a grid

        # Fill arrays
        for line in f.readlines():
            x1, y1, x2, y2 = line[0:-1].split(" ")
            x_array.append(int(x1))
            x_array.append(int(x2))
            y_array.append(int(y1))
            y_array.append(int(y2))

            rect_array.append([int(x1), int(y1), int(x2), int(y2)])

    # Remove duplicates and sort arrays
    x_array = list(set(sorted(x_array)))
    y_array = list(set(sorted(y_array)))

    print(type(x_array))


    def square(rectangle):
        return (rectangle[2] - rectangle[0]) * (rectangle[3] - rectangle[1])  # (x2-x1)*(y2-y1)


    def check_rectangle(mesh):
        for rectangle in rect_array:
            if (mesh[2] >= rectangle[0] and mesh[2] <= rectangle[2]) and (
                            mesh[3] >= rectangle[1] and mesh[3] <= rectangle[3]):
                return True
        return False


    result = 0
    # Go through x-array:
    for i in range(len(x_array)-1):
        for j in range(len(y_array)-1):
            mesh = [x_array[i], y_array[j], x_array[i + 1], y_array[j + 1]]
            if check_rectangle(mesh):
                result += square(mesh)

                # Go through y-array:
                # Check if rectangle x1x2y1y2 is in target figure
                # If it is:
                # Result += square of rectangle

print(result)







