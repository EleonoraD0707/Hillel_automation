import math

# Define an abstract class Figure
class Figure:
    def __init__(self):
        pass

    def perimeter(self):
        pass

    def square(self):
        pass

# Inherit Triangle from Figure
class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = 5
        self.b = 5
        self.c = 5

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# Inherit Round (Circle) from Figure
class Round(Figure):
    def __init__(self, radius):
        self.radius = 7

    def perimeter(self):
        return 2 * math.pi * self.radius

    def square(self):
        return math.pi * self.radius**2

# Create a collection of Figures
figures = [Triangle(3, 4, 5), Round(2), Triangle(6, 8, 10), Round(3)]

# Calculate the total perimeter and square of the figures
total_perimeter = sum(figure.perimeter() for figure in figures)
total_square = sum(figure.square() for figure in figures)

# Print the results
print("Total Perimeter:", total_perimeter)
print("Total Square:", total_square)
