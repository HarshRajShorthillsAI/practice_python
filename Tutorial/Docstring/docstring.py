def add(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of a and b.
    """
    return a + b

class Circle:
    """
    A class to represent a circle.

    Attributes:
    radius (float): The radius of the circle.

    Methods:
    area(): Returns the area of the circle.
    circumference(): Returns the circumference of the circle.
    """

    def __init__(self, radius):
        """
        Initializes a Circle instance with the given radius.

        Parameters:
        radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Returns the area of the circle."""
        return 3.14159 * self.radius ** 2

    def circumference(self):
        """Returns the circumference of the circle."""
        return 2 * 3.14159 * self.radius
