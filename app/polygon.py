from config import Shape


class Polygon:
    def __init__(self, coordinates, name):
        self.coordinates = coordinates
        self.name = name
        self.number_points = len(self.coordinates)
        self.polygon_type = Shape(self.number_points).name
