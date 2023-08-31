import math
import sys


def Ginput():
    try:
        inputs = list(map(float, input("Enter the measurements: ").split()))

    except ValueError or NameError or UnboundLocalError:
        print("Enter only positive integer.")

    return inputs




class Shape():
    def calculate_area(self):
        pass


class Square(Shape):
    def calculate_area(self, side):
        return side ** 2


class Triangle(Shape):
    def calculate_area(self, side1, side2, side3):
        s = (side1 + side2 + side3) / 2
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))


class Circle(Shape):
    def calculate_area(self, radius):
        return math.pi * radius ** 2


inputs = Ginput()


if len(inputs) == 1:
    shape = Circle()
    if inputs[0] <= 0:
        print("Enter valid positive input.")
        sys.exit()
    area = shape.calculate_area(inputs[0])
    print(f"The area of the circle is: {area}")
elif len(inputs) == 2:
    shape = Square()
    for i in range(2):
        if inputs[i] <= 0:
            print("Enter valid positive input.")
            sys.exit()
    area = shape.calculate_area(inputs[0])
    print(f"The area of the square is: {area}")
elif len(inputs) == 3:
    shape = Triangle()
    for i in range(3):
        if inputs[i] <= 0:
            print("Enter valid positive input.")
            sys.exit()
    area = shape.calculate_area(inputs[0], inputs[1], inputs[2])
    print(f"The area of the triangle is: {area}")
else:
    print("Enter valid argument.")