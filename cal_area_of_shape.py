import math
import sys


def Ginput():
    try:
        inputs = input("Enter the measurements: ").split()

        if len(inputs) < 1 or len(inputs) > 3:
            raise ValueError("Enter 1 to 3 positive values.")

        if len(inputs) == 3 and inputs[2].lower() != "t":
            raise ValueError("Invalid input for a triangle. Use 'T' for triangle.")

        # for value in inputs[:2]:
        #     if not value.replace('.', '', 1).isdigit() or float(value) <= 0:
        #         raise ValueError("Enter only positive numeric values.")

        return inputs

    except ValueError:
        print("Invalid input. Please enter 1 to 3 positive numeric values with 'T' for triangle.")
        sys.exit()





class Square():
    def calculate_area(self, **kwargs):
        side = kwargs.get("side")
        return side ** 2


class Triangle():
    def calculate_area(self, **kwargs):
        if all(key in kwargs for key in ["base", "height", "shape_type"]) and kwargs["shape_type"].lower() == "t":
            base = kwargs["base"]
            height = kwargs["height"]
            return 0.5 * base * height
        else:
            raise ValueError("Invalid arguments for a triangle.")


class Circle():
    def calculate_area(self, radius):
        return math.pi * radius ** 2


inputs = Ginput()

shape = None

if len(inputs) == 1:
    shape = Circle()
    area = shape.calculate_area(radius=float(inputs[0]))
elif len(inputs) == 2:
    shape = Square()
    area = shape.calculate_area(side=float(inputs[0]))
elif len(inputs) == 3:
    shape_type = inputs[2].lower()
    if shape_type == "t":
        shape = Triangle()
        area = shape.calculate_area(base=float(inputs[0]), height=float(inputs[1]), shape_type=shape_type)
    else:
        print("Invalid shape type. Use 'T' for triangle.")
        sys.exit()
else:
    print("Invalid number of arguments. Please enter 1 to 3 positive numeric values.")

if shape:
    print(f"The area is: {area}")
