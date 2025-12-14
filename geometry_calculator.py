import math

class GeometryCalculator:
    def circle_area(self, radius):
        return math.pi * radius * radius

    def rectangle_area(self, length, width):
        return length * width


if __name__ == "__main__":
    g = GeometryCalculator()
    print("Circle Area:", g.circle_area(5))
    print("Rectangle Area:", g.rectangle_area(10, 6))
