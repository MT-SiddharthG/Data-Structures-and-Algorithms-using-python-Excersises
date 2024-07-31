import math

class InvalidCoordinateError(Exception):
    """Raised when an invalid coordinate value is provided."""
    pass

class Point:
    """
    Represents a point in a two-dimensional space.
    
    Attributes:
        xCoord (float): The x-coordinate of the point.
        yCoord (float): The y-coordinate of the point.
    """

    def __init__(self, x=0, y=0):
        """
        Initializes a Point object with coordinates (x, y).
        
        Args:
            x (float): The x-coordinate. Defaults to 0.
            y (float): The y-coordinate. Defaults to 0.
            
        Raises:
            InvalidCoordinateError: If either x or y is not a number.
        """
        self.xCoord = self._validate_coordinate(x)
        self.yCoord = self._validate_coordinate(y)

    def _validate_coordinate(self, coord):
        """Validates if the coordinate is a number."""
        if isinstance(coord, (int, float)):
            return coord
        raise InvalidCoordinateError("Coordinate must be a number")

    def getX(self):
        """Returns the x-coordinate of the point."""
        return self.xCoord

    def getY(self):
        """Returns the y-coordinate of the point."""
        return self.yCoord

    def shift(self, xInc=0, yInc=0):
        """
        Shifts the point by xInc and yInc.
        
        Args:
            xInc (float): The increment in x-coordinate. Defaults to 0.
            yInc (float): The increment in y-coordinate. Defaults to 0.
            
        Raises:
            InvalidCoordinateError: If either xInc or yInc is not a number.
        """
        self.xCoord += self._validate_coordinate(xInc)
        self.yCoord += self._validate_coordinate(yInc)

    def distance(self, otherPoint):
        """
        Computes the distance between this point and another point.
        
        Args:
            otherPoint (Point): The other point to compute distance against.
            
        Returns:
            float: The Euclidean distance between the two points.
            
        Raises:
            TypeError: If otherPoint is not an instance of Point.
        """
        if not isinstance(otherPoint, Point):
            raise TypeError("otherPoint must be an instance of Point")
        
        xDiff = self.xCoord - otherPoint.xCoord
        yDiff = self.yCoord - otherPoint.yCoord
        return math.sqrt(xDiff ** 2 + yDiff ** 2)

    def inverse(self):
        """
        Creates a new point that is the inverse of this point (i.e., x and y values swapped).
        
        Returns:
            Point: The inverse point.
        """
        return Point(self.yCoord, self.xCoord)

    def __repr__(self):
        """Returns a string representation of the point."""
        return f"Point({self.xCoord}, {self.yCoord})"

    def __eq__(self, other):
        """Checks if this point is equal to another point."""
        if isinstance(other, Point):
            return self.xCoord == other.xCoord and self.yCoord == other.yCoord
        return False

if __name__ == "__main__":
    # Examples
    p1 = Point(3, 4)
    print(f"Original Point 1: {p1}")

    p2 = Point(3, 4)
    print(f"Original Point 2: {p2}")
    
    p3 = p1.inverse()
    print(f"Inverse of Point 1(P3): {p3}")
    
    print(f"Distance between Original P1 and P3: {p1.distance(p3)}")
    
    print(f"Distance between Original P1 and Original P2: {p1.distance(p2)}")
    try:
        p3 = Point("a", 5)
    except InvalidCoordinateError as e:
        print(e)

    print(f"P1 equals P2? {p1 == p2}")

    p1.shift(1, -1)
    print(f"Shifted Point 1 by (1, -1): {p1}")

    print(f"P1 equals P2 after shifting? {p1 == p2}")

    print(f"P1 equals P3? {p1 == p3}")
