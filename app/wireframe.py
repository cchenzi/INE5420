from utils import Shape


class Wireframe:
    def __init__(self, coordinates, index, color):
        self.coordinates = coordinates
        self.number_points = len(self.coordinates)
        self.polygon_type = Shape(self.number_points).name
        self.name = f"{self.polygon_type}_{index}"
        self.color = color
