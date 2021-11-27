class Point:
    """ represents a point in 2-D geometric coordinates """

    def __init__(self, x=0, y=0):
        """
        initializes the position of a new point. the x  and y  coordinates can be specified.
        if they are not, the point defaults to the origin
        """
        self.move(x, y)

    def reset(self):
        """
        Reset the point back to the geometric origin: 0, 0
        """
        self.move(0, 0)

    def move(self, x, y):
        """move the point back to a new location in 2D space """
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        """
        Calculate the distance from this point to a second point passed as a parameter.
        This function uses the Pythagorean Theorem to calculate the distance between the two points.
        the distance is returned as a float.
        """
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5
