from PointADT import Point

class Polygon:
    """
    Represents a polygon with vertices defined as points.
    
    Attributes:
        vertices (list): A list of Point objects representing the vertices of the polygon.
        num_sides (int): The number of sides in the polygon.
    """

    def __init__(self, vertices):
        """
        Initializes a Polygon object with a list of vertices.
        
        Args:
            vertices (list): A list of Point objects defining the vertices of the polygon.
        """

        if not all(isinstance(vertex, Point) for vertex in vertices):
            raise ValueError("All vertices must be instances of Point.")
        if len(vertices) < 3:
            raise ValueError("A polygon must have at least 3 vertices.")
        
        # # Check if vertices form a valid polygon by verifying closure
        # if vertices[0] != vertices[-1]:
        #     raise ValueError("Vertices must form a closed shape to represent a polygon.")
        
        self.vertices = vertices
        self.num_sides = len(vertices)

    def __str__(self):
        """
        Returns a string representation of the polygon, including its name based on the number of sides.
        """

        side_count = self.num_sides
        if side_count == 3:
            return f"Triangle({self.vertices})"
        elif side_count == 4:
            return f"Quadtrilateral({self.vertices})"
        elif side_count == 5:
            return f"Pentagon({self.vertices})"
        else:
            return f"Polygon({self.vertices})"
        

    def get_vertices(self):
        """
        Returns the list of vertices of the polygon.
        
        Returns:
            list: The list of vertices.
        """
        return self.vertices

    def get_num_sides(self):
        """
        Returns the number of sides in the polygon.
        
        Returns:
            int: The number of sides.
        """
        return self.num_sides

    def area(self):
        """
        Calculates and returns the area of the polygon.
        
        Returns:
            float: The area of the polygon.
        """
        n = self.num_sides
        area = 0
        for i in range(n):
            j = (i + 1) % n
            area += self.vertices[i].xCoord * self.vertices[j].yCoord
            area -= self.vertices[j].xCoord * self.vertices[i].yCoord
        return abs(area) / 2

    def perimeter(self):
        """
        Calculates and returns the perimeter of the polygon.
        
        Returns:
            float: The perimeter of the polygon.
        """
        perimeter = 0
        for i in range(self.num_sides):
            j = (i + 1) % self.num_sides
            perimeter += ((self.vertices[i].xCoord - self.vertices[j].xCoord) ** 2 +
                          (self.vertices[i].yCoord - self.vertices[j].yCoord) ** 2) ** 0.5
        return perimeter

    def is_convex(self):
        """
        Determines whether the polygon is convex.
        
        Returns:
            bool: True if the polygon is convex, False otherwise.
        """
        n = self.num_sides
        sign = 0
        for i in range(n):
            j = (i + 1) % n
            k = (i + 2) % n
            cross_product = (self.vertices[j].xCoord - self.vertices[i].xCoord) * (self.vertices[k].yCoord - self.vertices[j].yCoord) - \
                             (self.vertices[j].yCoord - self.vertices[i].yCoord) * (self.vertices[k].xCoord - self.vertices[j].xCoord)
            if sign == 0:
                sign = cross_product
            elif sign * cross_product < 0:
                return False
        return True

    def contains_point(self, point):
        """
        Checks if a given point is inside the polygon.
        
        Args:
            point (Point): The point to check.
            
        Returns:
            bool: True if the point is inside the polygon, False otherwise.
        """
        n = self.num_sides
        inside = False
        p1xCoord, p1yCoord = self.vertices[0].xCoord, self.vertices[0].yCoord
        for i in range(n + 1):
            p2xCoord, p2yCoord = self.vertices[i % n].xCoord, self.vertices[i % n].yCoord
            if point.yCoord > min(p1yCoord, p2yCoord):
                if point.yCoord <= max(p1yCoord, p2yCoord):
                    if point.xCoord <= max(p1xCoord, p2xCoord):
                        if p1yCoord != p2yCoord:
                            xinters = (point.yCoord - p1yCoord) * (p2xCoord - p1xCoord) / (p2yCoord - p1yCoord) + p1xCoord
                        if p1xCoord == p2xCoord or point.xCoord <= xinters:
                            inside = not inside
            p1xCoord, p1yCoord = p2xCoord, p2yCoord
        return inside


if __name__ == '__main__':
    
    # Define vertices for a simple triangle
    vertices = [Point(0, 0), Point(8, 2), Point(5, 5)]
    polygon = Polygon(vertices)

    vertices_square = [Point(0, 0), Point(4, 0), Point(4, 4), Point(0, 4)]
    polygon_square = Polygon(vertices_square)
    
    print(polygon)

    # Display basic information about the polygon
    print(f"Vertices1: {polygon.get_vertices()}")
    print(f"Number of Sides1: {polygon.get_num_sides()}")

    # Calculate and display the area and perimeter
    print(f"Area: {polygon.area()}")
    print(f"Perimeter: {polygon.perimeter()}")

    # Check if the polygon is convex
    print(f"Is Convex: {polygon.is_convex()}")

    # Attempt to contain a point inside the polygon
    point_inside = Point(0.5, 0.5)
    print(f"Does the polygon contain the point ({point_inside.xCoord}, {point_inside.yCoord})? {polygon.contains_point(point_inside)}")

    print(f"Vertices2: {polygon_square.get_vertices()}")
    print(f"Number of Sides2: {polygon_square.get_num_sides()}")

    # Calculate and display the area and perimeter
    print(f"Area2: {polygon_square.area()}")
    print(f"Perimeter2: {polygon_square.perimeter()}")

    # Check if the polygon_square is convex
    print(f"Is Convex2: {polygon_square.is_convex()}")

    # Attempt to contain a point inside the polygon
    point_inside = Point(1, 2)
    print(f"Does the polygon_square contain the point ({point_inside.xCoord}, {point_inside.yCoord})? {polygon_square.contains_point(point_inside)}")
