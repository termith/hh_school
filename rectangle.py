import sys

class Rectangle(object):
    def __init__(self, coordinates):
        self.x_AB = int(coordinates[0])
        self.x_CD = int(coordinates[1])
        self.y_AD = int(coordinates[2])
        self.y_BC = int(coordinates[3])

    def square(self):
        return (self.x_CD - self.x_AB)*(self.y_BC - self.y_AD)


# Fill list of rectangles
with open("D:\\rectangles.txt") as f:
    rect_list = []
    for line in f.readlines():
        rect_list.append(Rectangle(line[0:-1].split(" ")))
i = 0
common_square = 0
while i < len(rect_list):
    first_rect = rect_list[i]
    second_rect = rect_list[i+1]

    if first_rect.x_CD <= second_rect.x_AB: #Не пересекаются, первый правее второго
        common_square += first_rect.square() + second_rect.square() 










