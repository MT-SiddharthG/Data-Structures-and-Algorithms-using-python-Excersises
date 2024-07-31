from PointADT import Point
import math

class InvalidPointError(Exception):
    """Raised when an invalid Point object is passed."""
    pass

class LineSegment:
    def __init__(self, ptA: Point, ptB: Point):
        """
        Initializes a LineSegment object with endpoints ptA and ptB.
        
        Args:
            ptA (Point): The first endpoint of the line segment.
            ptB (Point): The second endpoint of the line segment.
            
        Raises:
            InvalidPointError: If either ptA or ptB is not a valid Point object.
        """
        if not isinstance(ptA, Point) or not isinstance(ptB, Point):
            raise InvalidPointError("Both endpoints must be instances of Point.")
        self.ptA = ptA
        self.ptB = ptB

    def __repr__(self):
        """Returns a string representation of the line segment."""
        return f"LineSeg({self.ptA!r}, {self.ptB!r})"

    def __eq__(self, other):
        """Checks if this line segment is equal to another line segment."""
        if isinstance(other, LineSegment):
            return self.ptA == other.ptA and self.ptB == other.ptB
        return False

    def __add__(self, other):
        """Adds another line segment or shifts this line segment by a vector."""
        if isinstance(other, LineSegment):
            return LineSegment(
                Point(self.ptA.xCoord + other.ptA.xCoord, self.ptA.yCoord + other.ptA.yCoord),
                Point(self.ptB.xCoord + other.ptB.xCoord, self.ptB.yCoord + other.ptB.yCoord)
            )
        elif isinstance(other, tuple) and len(other) == 2:
            dxCoord, dyCoord = other
            return LineSegment(
                Point(self.ptA.xCoord + dxCoord, self.ptA.yCoord + dyCoord),
                Point(self.ptB.xCoord + dxCoord, self.ptB.yCoord + dyCoord)
            )
        else:
            raise TypeError("Unsupported operand type for addition")

    def endPointA(self):
        """Returns the first endpoint of the line segment."""
        return self.ptA

    def endPointB(self):
        """Returns the second endpoint of the line segment."""
        return self.ptB

    def length(self):
        """Calculates the length of the line segment."""
        dxCoord = self.ptB.xCoord - self.ptA.xCoord
        dyCoord = self.ptB.yCoord - self.ptA.yCoord
        return math.sqrt(dxCoord * dxCoord + dyCoord * dyCoord)

    def isVertical(self):
        """Checks if the line segment is vertical."""
        return self.ptA.xCoord == self.ptB.xCoord

    def isHorizontal(self):
        """Checks if the line segment is horizontal."""
        return self.ptA.yCoord == self.ptB.yCoord

    def slope(self):
        """Calculates the slope of the line segment."""
        dxCoord = self.ptB.xCoord - self.ptA.xCoord
        dyCoord = self.ptB.yCoord - self.ptA.yCoord
        if dxCoord == 0:
            return None  # Vertical line has undefined slope
        else:
            return dyCoord / dxCoord

    def shift(self, xInc, yInc):
        """Shifts both endpoints of the line segment by xInc and yInc."""
        self.ptA.xCoord += xInc
        self.ptA.yCoord += yInc
        self.ptB.xCoord += xInc
        self.ptB.yCoord += yInc

    def midpoint(self):
        """Calculates the midpoint of the line segment."""
        mid_xCoord = (self.ptA.xCoord + self.ptB.xCoord) / 2
        mid_yCoord = (self.ptA.yCoord + self.ptB.yCoord) / 2
        return Point(mid_xCoord, mid_yCoord)

    def isParallel(self, other):
        """Checks if the line segment is parallel to another line segment."""
        if self.isVertical() and other.isVertical():
            return True
        elif self.isHorizontal() and other.isHorizontal():
            return True
        else:
            return self.slope() == other.slope()
        
    def isPerpendicular(self, other):
        """Checks if the line segment is perpendicular to another line segment."""
        if self.isVertical() and other.isHorizontal():
            return True
        elif self.isHorizontal() and other.isVertical():
            return True
        else:
            return self.slope() == -1 / other.slope()
        
        

if __name__ == '__main__':
    # Creating points
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p3 = Point(5, 6)

    p4 = Point(2, 2)
    p5 = Point(3, 5)

    p6 = Point(4, 1)
    p7 = Point(5, 4)

    # Creating line segments
    l1 = LineSegment(p1, p2)
    l2 = LineSegment(p2, p3)
    l3 = LineSegment(p4, p5)
    l4 = LineSegment(p6, p7)

    # Example usage of methods
    print(f"Creating LineSegment1 from Point({p1.xCoord}, {p1.yCoord}) to Point({p2.xCoord}, {p2.yCoord}): {l1}")
    print(f"Checking if LineSegment1 is equal to LineSegment2: {l1 == l2}")
    print(f"Adding LineSegment1 and LineSegment2 : {l1 + l2}")
    l1.shift(1, 1)
    print(f"Shifting LineSegment1 by (1, 1): {l1}")
    print(f"Getting the first endpoint of LineSegment1 : {l1.endPointA()}")
    print(f"Getting the second endpoint of LineSegment1 : {l1.endPointB()}")
    print(f"Calculating the length of LineSegment1 : {l1.length()} units")
    print(f"Checking if LineSegment1 is vertical: {'Yes' if l1.isVertical() else 'No'}")
    print(f"Checking if LineSegment1 is horizontal: {'Yes' if l1.isHorizontal() else 'No'}")
    print(f"Finding the midpoint of LineSegment1 {l1}: {l1.midpoint()}")

    print(f"Check if {l3} is parallel to {l4}: {l3.isParallel(l4)}")